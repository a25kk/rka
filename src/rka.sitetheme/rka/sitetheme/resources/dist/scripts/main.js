requirejs(['require',
'/++theme++rka.sitetheme/dist/scripts/flickity.pkgd.js',
'/++theme++rka.sitetheme/dist/scripts/fontfaceobserver.js',
'/++theme++rka.sitetheme/dist/scripts/hideShowPassword.js',
'/++theme++rka.sitetheme/dist/scripts/jvfloat.js',
'/++theme++rka.sitetheme/dist/scripts/respimage.js',
'/++theme++rka.sitetheme/dist/scripts/ls.parent-fit.js',
'/++theme++rka.sitetheme/dist/scripts/lazysizes-umd.js',],
 function(require, Flickity) {
'use strict';
var font = new FontFaceObserver('Open Sans');
font.load().then(function () {
    document.documentElement.className += " app-fonts-loaded";
});
var $bannerBar = document.querySelectorAll('.app-js-carousel'),
    $galleryContainer = document.querySelectorAll('.js-gallery');
if ($bannerBar.length) {
    var bannerflkty = new Flickity('.app-js-carousel', {
        autoPlay: 7000,
        contain: true,
        wrapAround: true,
        imagesLoaded: true,
        cellSelector: '.app-banner-item',
        cellAlign: 'left',
        selectedAttraction: 0.025,
        friction: 0.28
    });
}
// Content image galleries
if ($galleryContainer.length) {
    var flkty = new Flickity('.js-gallery', {
        autoPlay: true,
        contain: true,
        wrapAround: true,
        imagesLoaded: true,
        cellSelector: '.app-gallery-cell',
        cellAlign: 'left'
    });
}
// Anonymous only scripts (mainly used in login views)
if ($(".userrole-anonymous")[0]) {
    // Show password by default
    $('input[type="password"]').hideShowPassword(true, 'focus');
    //$('input[type="password"]').showPassword('focus', {});
    // Float labels (requires corresponding css)
    $('.app-signin-input').jvFloat();

};
});