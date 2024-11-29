<!DOCTYPE html>
<html lang="en">
    <title>latihan html</title>
<head>
    
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <h1>WEBSITE AL</h1>
</head>
<body>
    <div>
        Nama: Romy
    </div>
    <div>
        Kelas: Fase E PPLG
    </div>


    <table border="2">
        
            <tr>
                <td>NO ABSEN</td>
                <td>NAMA</td>
                <td>MATA PELAJARAN</td>
                </tr>
                <td>31</td>
                <td>Romy Al Ghazaly</td>
                <td>Dasar PPLG</td>
            <tr>
                <td>25</td>
                <td>Pian</td>
                <td>Dasar PPLG</td>
    </table>
    <br>
    <div>
        <form>
            <label>Username:</label>
            <input type="text" name="username">
            <label for="passwordd">passwordd</label>
            <input type="password" name="passwordd">
        </form>
    </div>
    <br>
    <div>
        <label for="gender">Gender</label><br>
        <input type="radio" name="gender">Laki-laki<br>
        <input type="radio" name="gender">Perempuan<br>
        <input type="radio" name="gender">Bencong<br>
        <input type="radio" name="gender">Banci<br>
    </div>
    <label for="hobi">Hobby</label><br>
    <input type="checkbox" name="hobi">Silat<br>
    <input type="checkbox" name="hobi">Sepak Bola<br>
    <input type="checkbox" name="hobi">Volly<br>
    <input type="checkbox" name="hobi">Gamers<br>
    <br>
    <div>
        <label>Foto Al:</label><br>
        <img src="foto.jpg" width="300px" height="200px" id="existingImage"><br><br>
        <label for="uploadFoto">Upload Foto:</label>
        <input type="file" id="uploadFoto" name="uploadFoto" onchange="previewImage(event)"><br><br>
        <img id="preview" width="200px" height="200px" style="display: none;"><br><br>
        <button>Upload Gambar</button>
        <input type="image" name="Gambar"><br><br>
        <button type="submit" name="login">Login</button>
    </div>
    <br>
    <script>
        function previewImage(event) {
            const preview = document.getElementById('preview');
            preview.src = URL.createObjectURL(event.target.files[0]);
            preview.style.display = 'block';
        }
    </script>
</body>
</html>