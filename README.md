<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Restaurante Sabor & Grill</title>

  <style>
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background: #f5f5f5;
    }

    header {
      background: #8B0000;
      color: white;
      text-align: center;
      padding: 20px;
    }

    nav {
      background: #333;
      display: flex;
      justify-content: center;
    }

    nav a {
      color: white;
      padding: 15px;
      text-decoration: none;
    }

    nav a:hover {
      background: #555;
    }

    .banner {
      background: url('https://images.unsplash.com/photo-1555992336-03a23c9f2f80') no-repeat center/cover;
      height: 300px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-size: 30px;
      font-weight: bold;
    }

    .container {
      padding: 20px;
      text-align: center;
    }

    .card {
      background: white;
      padding: 20px;
      margin: 10px;
      display: inline-block;
      width: 250px;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }

    button {
      background: #8B0000;
      color: white;
      border: none;
      padding: 10px;
      border-radius: 5px;
      cursor: pointer;
    }

    footer {
      background: #333;
      color: white;
      text-align: center;
      padding: 10px;
      margin-top: 20px;
    }
  </style>
</head>

<body>

<header>
  <h1>🍔 Sabor & Grill</h1>
  <p>O melhor da comida na sua mesa</p>
</header>

<nav>
  <a href="#">Início</a>
  <a href="#">Cardápio</a>
  <a href="#">Contato</a>
</nav>

<div class="banner">
  Bem-vindo ao melhor restaurante!
</div>

<div class="container">
  <h2>Nosso Cardápio</h2>

  <div class="card">
    <h3>🍔 Hambúrguer</h3>
    <p>Delicioso hambúrguer artesanal</p>
    <button onclick="pedir('Hambúrguer')">Pedir</button>
  </div>

  <div class="card">
    <h3>🍕 Pizza</h3>
    <p>Pizza quentinha e recheada</p>
    <button onclick="pedir('Pizza')">Pedir</button>
  </div>

  <div class="card">
    <h3>🥤 Refrigerante</h3>
    <p>Bebidas geladas</p>
    <button onclick="pedir('Refrigerante')">Pedir</button>
  </div>

  <p id="msg" style="margin-top:20px;"></p>
</div>

<footer>
  <p>© 2026 Sabor & Grill</p>
</footer>

<script>
  function pedir(item) {
    document.getElementById("msg").innerHTML =
      "Pedido de <b>" + item + "</b> realizado! ✅";
  }
</script>

</body>
</html>
