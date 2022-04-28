<?php
if (isset($_POST['submit'])){
    $file = $_FILES['file'];

    $fileName = $_FILES['file']['name'];
    $fileTmpName = $_FILES['file']['tmp_name'];
    $fileSize = $_FILES['file']['size'];
    $fileError = $_FILES['file']['error'];
    $fileType = $_FILES['file']['type'];

    $fileExt = explode('.', $fileName);
    $fileActualExt = strtolower(end($fileExt));

    $allowed = array('sc2replay');

    if (in_array($fileActualExt, $allowed)){
        if ($fileError === 0){
            $fileNameNew = uniqid('', true).".".$fileActualExt;
            $fileDestination = 'replays/'.$fileNameNew;
            move_uploaded_file($fileTmpName, $fileDestination);
            header("Location: replays.html?successfulUpload");
        }
        else{
            echo "ERROR";
        }
    }
    else{
        echo "You can ONLY upload '.SC2Replay' files";
    }   
}