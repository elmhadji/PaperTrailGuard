# PaperTrailGuard

## Description
PaperTrailGuard is a dual-platform solution for reducing paper fraud. It includes a Python desktop app (or Script) to generate QR codes for documents, and a React Native mobile app to scan and verify these codes.

## Installation
1. Clone the repository.
```copy
git clone https://github.com/elmhadji/PaperTrailGuard
```

### Desktop App
1. Install the required Python packages by running.
```copy 
pip install -r desktop_app/requirements.txt
```
2. To start the application run.
```copy 
python desktop_app/main.py
```

### Mobile App
1. Navigate to the `mobile_app` directory.
```copy
cd mobile_app/
```
2. Install the required npm packages by running.
```copy 
npm install
```
3. To start the development server run.
```copy 
npx expo start
```

## Usage

### Desktop App
- Login by simply using `admin` as `username` and `password`
- Manages Students Information
- Preview Students Information
- Print PDF file contain encrypted QR codes for each student.

### Mobile App
- Open the app on your mobile device.
- Scan QR codes to verify document authenticity.


## Integrating into your system
You don't need the desktop application if you want to integrate into your system. You can check the script in `script/python generate_qr_code.py`.

## License
This project is licensed under the MIT License - see the `LICENSE.md` file for details.
