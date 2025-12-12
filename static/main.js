$(document).ready(function () {

  // Ini fungsinya untuk load navbar.html ke dalam #navbar-ppm
  $("#navbar-ppm").load("components/navbar.html", function () {
    let currentPath = window.location.pathname;

    // Ambil hanya bagian terakhir dari path (file name). Udah di tes case dengan banyak skenario
    // termasuk kalo nanti ada subfolder di dalam folder untuk mencari index.html
    currentPath = currentPath.endsWith("/") ? "index.html" : currentPath.split("/").pop();

    // Bersihkan semua dulu. Tujuannya biar ketika load pertama semua navbar dan dropdown item ga aktif
    $(".navbar .nav-link").removeClass("active");
    $(".dropdown-item").removeClass("active");

    // 1. Aktifkan nav biasa
    $(".navbar .nav-link").each(function () {
      const linkPath = $(this).attr("href");
      if (linkPath === currentPath) {
        $(this).addClass("active");
      }
    });

    // 2. Aktifkan dropdown
    $(".dropdown-item").each(function () {
      const linkPath = $(this).attr("href");
      if (linkPath === currentPath) {
        $(this).addClass("active");
        $(this).closest(".dropdown").find(".nav-link.dropdown-toggle").addClass("active");
      }
    });

  });

  // Memunculkan footer disemua halaman
  $("#footer-ppm").load("components/footer.html");

  // Animasi Fade down
  // $(window).scroll(function () {
  //   const element = document.querySelector('.fade-down-in-on-scroll');
  //   const elementPosition = element.getBoundingClientRect().top;
  //   const screenPosition = window.innerHeight / 1.3;

  //   if (elementPosition < screenPosition) {
  //     element.classList.add('animate');
  //   }
  // });

  // Animasi card yang pop-up ketika kita nge scroll
  $(window).scroll(function () {
    const cards = document.querySelectorAll('.card');
    const screenPosition = window.innerHeight / 1.3;

    cards.forEach(card => {
      const cardPosition = card.getBoundingClientRect().top;

      if (cardPosition < screenPosition) {
        card.classList.add('pop-up');
      }
    });
  });

  // Fungsi tentang turn on background color di navbar dan adanya tombol back-to-top. Dan juga kasih shadow kalo scroll
  $(window).scroll(function () {
    var scroll = $(window).scrollTop();
    if (scroll > 50) {
      $(".navbar").css({
        "background-color": "var(--primary-color)",
        "box-shadow": "0 2px 10px rgba(0, 0, 0, 0.2)",
      });
      $(".back-to-top").addClass("active");
    }
    else {
      $(".navbar").css({
        "background-color": "transparent",
        "box-shadow": "none",
      });
      $(".back-to-top").removeClass("active");
    }
  });

  // Fungsi tentang menutup navbar setelah klik a link (offcanvas)
  $("#offcanvasDarkNavbar a").click(function () {
    if (!$(this).hasClass("dropdown-toggle")) {
      $('.offcanvas').offcanvas('hide');
    }
  });
});