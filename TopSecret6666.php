<?php
session_start();
if ($_COOKIE['sessionid'] == session_id(6666)) {
  echo "<body>
        Hi, darling! You are hacked!
        <script>
          window.opener.postMessage('TOP secret data', '*');
        </script>
        </body>";
} else {
  echo "Access denied";
}
