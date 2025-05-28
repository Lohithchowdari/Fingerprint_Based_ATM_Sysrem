import datetime
from tkinter.filedialog import askopenfilename
import cv2
from tkinter import Tk
from twilio.rest import Client
import mysql.connector 
import binary_processing_module as bmp
from inputimeout import inputimeout


conn = mysql.connector.connect(
    user='root',
    password='KLaftEEZoBvrSelyDyFsQXrgkjYLdmZA',
    host='crossover.proxy.rlwy.net',
    port=26866,
    database='railway',
    autocommit=True
)
connection_cursor = conn.cursor()
def second_authentication(acc_no,trial):    
            
    account_sid = "AC5d9a17af3729d2c2c5629546c4c477ea"
    auth_token = "2a43763eca18bb265f10dd114a236516"
    verify_sid = "VAccae5f422e201e444628e9ac3122c885"
    verified_number = "+918978188900"
    client = Client(account_sid, auth_token)
    print(f"📨 Sending OTP to: {verified_number}")
    client.verify.v2.services(verify_sid) \
    .verifications \
    .create(to=verified_number, channel="sms")

    try:
        otp_code = inputimeout(prompt="Please enter the OTP:", timeout=20)
    except Exception:
        print('Your time is over!')
        print('You have not entered the OTP')
        trial += 1
        if trial < 2:
            print("You have only one try   ")
        elif trial == 2:
            block_status_sql_query = """update ATM_database set block_status = %s, block_Time = %s where Account_no = %s"""
            current_time = datetime.datetime.now()
            block_status_tuple = ("Blocked",current_time,acc_no)
            connection_cursor.execute(block_status_sql_query,block_status_tuple)
            print("You have entered empty OTP twice ")
            print("Your Account has been blocked... \nContact your nearby bank to unblock your account ")
            exit()
        checking_finger_print(acc_no,trial)

    try:
        verification_check = client.verify.v2.services(verify_sid) \
        .verification_checks \
        .create(to=verified_number, code=otp_code)
        if verification_check.status == "approved":
            return True
        else:
            raise Exception

    except Exception:
        print("You have enterd wrong OTP")
        trial += 1
        if trial < 2:
            print("Your account will be blocked after one more wrong trial ")
        elif trial == 2:
            block_status_sql_query = """update ATM_database set block_status = %s, block_Time = %s where Account_no = %s"""
            current_time = datetime.datetime.now()
            block_status_tuple = ("Blocked",current_time,acc_no)
            connection_cursor.execute(block_status_sql_query,block_status_tuple)
            print("You have entered wrong OTP twice \nYour Account has been blocked... ")
            print("Contact your nearby Bank to unblock your account ")
            exit()
        checking_finger_print(acc_no,trial)

    
    
def checking_finger_print(account_no, trial=0):
    # Fetch fingerprint from DB
    search_finger_print_query = "SELECT finger_print FROM ATM_database WHERE Account_no = %s"
    connection_cursor.execute(search_finger_print_query, (account_no,))
    result_finegrprint = connection_cursor.fetchall()

    # Safe check: no result means no account found
    if not result_finegrprint:
        print(f"❌ No fingerprint found for account number: {account_no}")
        return False

    # Write stored binary to file
    proper_finger_print_after_writing = bmp.write_file(result_finegrprint[0][0], str(account_no) + ".jpeg")
    truth = True

    try:
        print("Place your finger on scanner ........")
        root = Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        scanned_finger_impression = askopenfilename(
            title="Select fingerprint image for authentication",
            filetypes=[("Image files", "*.bmp *.jpg *.jpeg *.png")]
        )
        root.destroy()

        if not scanned_finger_impression:
            print("❌ No fingerprint selected. Try again.")
            return checking_finger_print(account_no, trial)

        sample = cv2.imread(scanned_finger_impression)
        fingerprint_image = cv2.imread(proper_finger_print_after_writing)

        sift = cv2.SIFT_create()
        keypoints_1, descriptors_1 = sift.detectAndCompute(sample, None)
        keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_image, None)

        matches = cv2.FlannBasedMatcher({'algorithm': 1, 'trees': 10}, {}).knnMatch(descriptors_1, descriptors_2, k=2)
        match_points = [p for p, q in matches if p.distance < 0.1 * q.distance]

        keypoints = min(len(keypoints_1), len(keypoints_2))
        best_score = (len(match_points) / keypoints) * 100 if keypoints else 0

        print(f"📊 Fingerprint match score: {best_score:.2f}")

        result = cv2.drawMatches(sample, keypoints_1, fingerprint_image, keypoints_2, match_points, None)
        result = cv2.resize(result, None, fx=2, fy=2)
        cv2.imshow("Fingerprint Match Result", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        if best_score < 80:
            print("❌ Low match score. Please scan your finger properly.")
            return checking_finger_print(account_no, trial)

    except Exception as e:
        truth = False
        print("❌ Fingerprint comparison failed.")
        print("Reason:", str(e))
        return checking_finger_print(account_no, trial)

    if truth:
        final_auth = second_authentication(account_no, trial)
        if not final_auth:
            return checking_finger_print(account_no, trial)

    return True
