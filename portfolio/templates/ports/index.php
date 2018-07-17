<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Page Title</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script>
    var btn = document.getElementById("btn_view");
    btn.onclick = function(e){
        //e.preventDefault();
        alert("Hello");
    }
    </script>
    <style>
        .container{
            width:60%;
            height:500px;
            margin:0 auto;
            background:#ff00ff;

        }
        .box{
            text-align:center;
            width:80%;
            margin:0 auto;
            font-size:30px;
            color:#fff;
            position:relative;
        }
    </style>
</head>
<body bgcolor="#FFF000">
    <h3 style="text-align:center">
        DJANGO WEB DEVELOPMENT FOR BEGINNERS
</h3>
<div class="container">
    <div class="box">
        javascript
        <button id="btn_view">Click Here</button>
    </div>
</div>
</body>
</html>