# Android APK Build Instructions

## Quick Setup

Your calculator app has been converted to an Android project. Here are the build options:

### Option 1: Using Android Studio (Recommended)
1. Install [Android Studio](https://developer.android.com/studio)
2. Open Android Studio
3. Select "Open an existing project"
4. Navigate to the `android-app` folder
5. Wait for Gradle sync to complete
6. Go to **Build > Generate Signed Bundle/APK > APK**
7. Choose "Debug" build type
8. Click "Finish"

### Option 2: Command Line (Requires Android SDK)
```bash
# Set Android SDK path
export ANDROID_HOME=/path/to/android/sdk

# Run the build script
./build-apk.sh
```

### Option 3: Online APK Builder
1. Zip the `android-app` folder
2. Use online services like:
   - MIT App Inventor
   - AppsGeyser
   - Appy Pie

## Project Structure
```
android-app/
├── app/
│   ├── src/main/
│   │   ├── java/com/calculator/MainActivity.java
│   │   ├── res/
│   │   │   ├── layout/activity_main.xml
│   │   │   ├── values/styles.xml
│   │   │   └── drawable/ic_launcher.xml
│   │   ├── assets/index.html
│   │   └── AndroidManifest.xml
│   └── build.gradle
├── gradle/wrapper/
├── build.gradle
└── settings.gradle
```

## Features
- ✅ WebView-based app with full calculator functionality
- ✅ Offline operation (no internet required)
- ✅ Dark mode support with local storage
- ✅ Responsive design for mobile devices
- ✅ All calculator types: Basic, Scientific, Programmer, Unit Converter

## Installation
Once built, install the APK on your Android device:
```bash
adb install app/build/outputs/apk/debug/app-debug.apk
```

## Troubleshooting
- Ensure Android SDK is installed and ANDROID_HOME is set
- Use Android Studio for easier building
- Check that Java 8+ is installed
- For online builders, ensure all files are included in the zip