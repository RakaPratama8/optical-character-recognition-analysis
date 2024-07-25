<html>
  <body>
    <header>
      <h1>Analisis teks pada foto menggunakan teknologi Optical Character Recognition (OCR)</h1>
      <p>Projek kali ini saya menganalisis suatu teks, berupa list nama, yang berada pada foto berformat <code>.jpg</code>, lalu mendapatkan suatu array berisi string dari nama - nama tersebut dengan menggunakan teknologi Optical Character Recognition (OCR).</p>
    </header>
    <main>
      <div id="daftarIsi">
        <h2>Daftar Isi</h2>
        <ul>
          <li><a href="#bahasa">Bahasa pemrograman</a></li>
          <li>
            <a href="#library">Library yang digunakan</a>
            <ul>
              <li><a href="#cv2">OpenCV</a></li>
              <li><a href="#plt">Matplotlib</a></li>
              <li><a href="#os">OS</a></li>
              <li><a href="#tess">Tesseract</a></li>
            </ul>
          </li>
          <li><a href="#code">Kode Program</a></li>
          <li><a href="#input">Foto yang dianalisa</a></li>
          <li><a href="#hasil">Hasil OCR</a></li>
        </ul>
      </div>
      <div id="bahasa">
        <h2>Bahasa Pemrograman</h2>
        <p>
          Bahasa pemrograman yang digunakan adalah <b>python</b>
        </p>
      </div>
      <div id="library">
        <h2>Library yang digunakan</h2>
        <p>Library yang digunakan pada projek ini antara lain</p>
        <ul>
          <li id="cv2">
            <h3>OpenCV</h3>
            <p><b>OpenCV (Open Source Computer Vision Library)</b>adalah sebuah library open-source yang digunakan untuk pemrosesan gambar dan visi komputer. Library ini mendukung berbagai bahasa pemrograman seperti Python, C++, dan Java. OpenCV menyediakan berbagai fungsi dan algoritma untuk operasi dasar seperti pengenalan objek, deteksi tepi, transformasi gambar, dan banyak lagi.</p>
          </li>
          <li id="plt">
            <h3>Pyplot</h3>
            <p>Pyplot adalah sebuah modul dalam library Matplotlib, yang digunakan untuk membuat visualisasi data seperti grafik dan plot. Pyplot memberikan antarmuka yang mirip dengan MATLAB, membuatnya mudah digunakan untuk membuat plot linier, histogram, scatter plot, dan berbagai jenis grafik lainnya. Ini sangat berguna untuk menampilkan data dan hasil analisis secara visual.</p>
          </li>
          <li id="os">
            <h3>OS</h3>
            <p>OS adalah sebuah modul standar dalam Python yang menyediakan berbagai fungsi untuk berinteraksi dengan sistem operasi. Modul ini memungkinkan Anda untuk melakukan operasi seperti membaca atau menulis file, memanipulasi direktori, dan menjalankan perintah sistem. OS modul sangat berguna untuk tugas-tugas yang melibatkan pengelolaan file dan direktori dalam sebuah program.</p>
          </li>
          <li id="tess">
            <h3>Tesseract</h3>
            <p>Tesseract adalah sebuah mesin OCR (Optical Character Recognition) yang sangat kuat dan open-source, awalnya dikembangkan oleh HP dan sekarang dikelola oleh Google. Tesseract digunakan untuk mengenali dan mengekstraksi teks dari gambar atau dokumen yang dipindai. Dalam Python, library pytesseract digunakan sebagai antarmuka untuk berinteraksi dengan Tesseract, membuatnya mudah untuk mengintegrasikan kemampuan OCR ke dalam aplikasi Python.</p>
          </li>
        </ul>
      </div>
      <div id="code">
        <h2>Kode Program</h2>
        <a href="https://github.com/RakaPratama8/optical-character-recognition-analysis/blob/master/ocr_process.ipynb">Klik Disini</a>
      </div>
      <div id="input">
        <h2>Foto Input</h2>
        <img src="https://github.com/RakaPratama8/optical-character-recognition-analysis/blob/master/data/list-of-names.jpg"></img>
      </div>
      <div id="hasil">
        <h2>Hasil OCR</h2>
        <p>Hasil ocr dapat dilihat pada bagian akhir program <a href="https://github.com/RakaPratama8/optical-character-recognition-analysis/blob/master/ocr_process.ipynb">disini</a> </p>
      </div>
    </main>
  </body>
</html>
