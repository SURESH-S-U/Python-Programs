<?php
require "phpqrcode/qrlib.php"; // Include QR code library

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $product = $_POST['product'];
    $price = $_POST['price'];
    $quantity = $_POST['quantity'];

    // Combine data to encode in QR
    $data = "Product: $product\nPrice: $price\nQuantity: $quantity";

    // Define QR code file path
    $file = "qrcodes/" . time() . ".png";

    // Generate QR Code
    QRcode::png($data, $file, QR_ECLEVEL_L, 5);

    echo "<h2>QR Code Generated</h2>";
    echo "<img src='$file' alt='QR Code'>";
    echo "<br><a href='index.php'>Generate Another</a>";
}
?>
