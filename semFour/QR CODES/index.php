<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QR Code Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
        }
        .container {
            max-width: 400px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        input, button {
            width: 100%;
            padding: 10px;
            margin-top: 10px;
        }
        img {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Generate QR Code</h2>
        <form action="generate_qr.php" method="POST">
            <input type="text" name="product" placeholder="Enter Product Name" required>
            <input type="number" name="price" placeholder="Enter Price" required>
            <input type="number" name="quantity" placeholder="Enter Quantity" required>
            <button type="submit">Generate QR Code</button>
        </form>
    </div>
</body>
</html>
