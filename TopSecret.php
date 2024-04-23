<?php
        if ($_COOKIE['sessionid'] == '261201081285') {
    echo "<body>
          Hi, darling! You are hacked!
          <script>
            window.opener.postMessage('TOP secret data', '*');
          </script>
          </body>";
  } else {
    echo "Access denied";
  }
?>
