<?php
// Start the session
session_start();

// Check if the session ID matches the expected value
if (session_id() == '261201081285') {
    // Generate a CSRF token
    if (empty($_SESSION['csrf_token'])) {
        $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
    }

    // Output the page content
    echo "<!DOCTYPE html>
            <html lang='en'>
            <head>
                <meta charset='UTF-8'>
                <meta http-equiv='Content-Security-Policy' content='default-src 'self'; script-src 'self';'>
                <title>Top Secret Page</title>
            </head>
            <body>
                Hi, darling! You are hacked!
                <script>
                    // Check if the parent window is from the same origin
                    if (window.opener && window.opener.location.origin === window.location.origin) {
                        // Send the secret data to the opener with a CSRF token
                        window.opener.postMessage({ secret: 'TOP secret data', csrfToken: '" . htmlspecialchars($_SESSION['csrf_token']) . "' }, '*');
                    }
                </script>
            </body>
            </html>";
} else {
    // Access denied
    echo "Access denied";
}
?>
