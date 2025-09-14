#!/bin/bash

echo "Building Android APK for Advanced Calculator..."

cd android-app

# Check if Android SDK is available
if [ -z "$ANDROID_HOME" ]; then
    echo "Error: ANDROID_HOME not set. Please install Android SDK and set ANDROID_HOME environment variable."
    echo "Alternative: Use Android Studio to build the APK"
    echo "1. Open Android Studio"
    echo "2. Open the 'android-app' folder as a project"
    echo "3. Build > Generate Signed Bundle/APK > APK"
    exit 1
fi

# Build the APK
echo "Building APK..."
./gradlew assembleDebug

if [ $? -eq 0 ]; then
    echo "✅ APK built successfully!"
    echo "📱 APK location: android-app/app/build/outputs/apk/debug/app-debug.apk"
    echo ""
    echo "To install on device:"
    echo "adb install app/build/outputs/apk/debug/app-debug.apk"
else
    echo "❌ Build failed. Please check the error messages above."
    echo ""
    echo "Alternative build methods:"
    echo "1. Use Android Studio to open the 'android-app' folder"
    echo "2. Use online APK builders like AppGeyser or AppsGeyser"
fi