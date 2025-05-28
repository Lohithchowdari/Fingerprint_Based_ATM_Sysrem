![image](https://github.com/user-attachments/assets/3bab2b67-d41b-4680-8948-6bf2a54e66da)# 🔐 Fingerprint-Based ATM Authentication System

This is a Python-based ATM project that uses a biometric authentication system. Along with fingerprint authentication, this project also includes OTP-based verification for secure two-step authentication.

> Secure ATM system using biometric fingerprint matching (OpenCV) and OTP (Twilio) verification.

## ✅ Features
- 🔒 Fingerprint-based authentication using OpenCV (SIFT + FLANN).
- 📲 OTP verification using Twilio API.
- 👤 User registration and login system.
- 💵 Secure money transactions: deposit, withdrawal.
- 🧾 Mini statement view.
- 🛡️ Account blocking after failed authentication attempts.

## 📂 Functionalities
Users will be able to:
- Register their account with fingerprint and details.
- Login using account number, fingerprint scan, and OTP.
- Withdraw and deposit money securely.
- View the mini statement with the latest transaction details.
- Automatic account block after 2 failed authentication attempts (requires manual unblock in MySQL).

## 🧬 Dataset

This project uses the **Sokoto Coventry Fingerprint Dataset (SOCOFing)** available on Kaggle.  
🔗 [Download Here](https://www.kaggle.com/datasets/ruizgara/socofing)

## 🛠 Tech Stack
- **Language:** Python
- **GUI:** Tkinter (for file selection dialogs)
- **Database:** MySQL (Railway DB)
- **Biometrics:** OpenCV (Fingerprint matching with SIFT + FLANN)
- **OTP SMS:** Twilio Verify API

## 📦 Required Libraries
```bash
pip install opencv-python
pip install mysql-connector-python
pip install twilio
pip install inputimeout
```

## 🚀 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Fingerprint_Based_ATM_Authentication_System.git
   cd Fingerprint_Based_ATM_Authentication_System
   ```

2. Install the dependencies mentioned above.

3. Configure Railway DB:
   - Ensure correct MySQL credentials are set in:
     - `ATM_authentication.py`
     - `login_module.py`
     - `registration_module.py`
     - `transaction_module.py`
   - Run:
     ```bash
     python test.py
     ```

4. Configure Twilio OTP:
   - Set your Twilio `account_sid`, `auth_token`, `verify_sid`, and verified phone number inside `ATM_authentication.py`.

5. Start the application:
   ```bash
   python ATM.py
   ```

> ⚠️ Ensure all configuration details are correct before running.

## 🗄️ MySQL Database Schema

Create a database `railway` and use the following table structure:

```sql
CREATE TABLE ATM_database (
  Sr_no INT AUTO_INCREMENT,
  first_name VARCHAR(20) NOT NULL,
  last_name VARCHAR(20) NOT NULL,
  phone_no BIGINT NOT NULL,
  Account_no BIGINT NOT NULL UNIQUE,
  finger_print LONGBLOB NOT NULL,
  Balance INT NOT NULL,
  Transaction TEXT NOT NULL,
  Amount INT NOT NULL,
  Date_Time DATETIME NOT NULL,
  block_status VARCHAR(10) NOT NULL,
  block_time DATETIME,
  PRIMARY KEY(Sr_no),
  CONSTRAINT con_1 UNIQUE(Account_no)
);
```

## 🧑‍💻 Screenshots

**Startup Interface:**
![image](https://github.com/user-attachments/assets/a6e30aa6-c843-44b9-bc1f-7567d832840b)


**Registration of Account:**
> ![image](https://github.com/user-attachments/assets/266487f5-aea1-4430-88bb-5f18bfe606c2)


**Authentication and Withdrawal:**
![image](https://github.com/user-attachments/assets/b52dc0c5-77c6-4a98-b432-b5c7672d9afe)

## 📌 Usage

1. Run `ATM.py`
2. Choose:
   - Registration
   - Login (with fingerprint + OTP)
3. Access banking operations:
   - Withdraw
   - Deposit
   - Mini Statement

## 📄 License

This project is licensed under the [MIT License](LICENSE).
