# User Dashboard with Location and Bluetooth Integration

This is a web-based user dashboard that allows users to view their profile, update details, see nearby users, fetch their location, and scan for nearby Bluetooth devices. It combines user interactivity with real-time geolocation and Web Bluetooth API functionalities.

---

## Features

- **User Profile Management**: 
  - Display username, phone number, and a profile picture generated dynamically using [RoboHash](https://robohash.org/).

- **Interactive Actions**:
  - Update username or user details.
  - View online and nearby users.
  - Logout securely.

- **Location Integration**:
  - Fetch the user's current geographic location (latitude and longitude).
  - Send location data to the backend for updates.

- **Bluetooth Integration**:
  - Scan for nearby Bluetooth devices using the Web Bluetooth API.
  - Display discovered devices in real-time.

- **Responsive Design**:
  - A user-friendly interface styled with CSS for a seamless experience.

---

## Technologies Used

- **Frontend**:
  - HTML5, CSS3, JavaScript (including Web APIs like Geolocation and Bluetooth).

- **Backend**:
  - Flask (for `url_for` routing, location updates, and backend integration).

- **APIs**:
  - Geolocation API for fetching user's location.
  - Web Bluetooth API for discovering nearby Bluetooth devices.

- **LLAMA 3.1 8B chat bot**:
  - Integrated a LLAMA 3.1 8B chat bot on the user_dashboard.html for direct easy interaction with an AI bot within the application
  
