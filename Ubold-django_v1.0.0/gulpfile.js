"use strict";

var gulp = require("gulp"),
  newer = require("gulp-newer"),
  imagemin = require("gulp-imagemin"),
  sass = require("gulp-sass"),
  sourcemaps = require("gulp-sourcemaps"),
  autoprefixer = require("gulp-autoprefixer"),
  cleanCSS = require("gulp-clean-css"),
  rename = require("gulp-rename"),
  concat = require("gulp-concat"),
  uglify = require("gulp-uglify"),
  npmdist = require("gulp-npm-dist"),
  rtlcss = require("gulp-rtlcss"),
  pjson = require("./package.json");
const minify = require("gulp-minify");

var app = "./" + pjson.name;

var folder = {
  src: app + "/static/", // source files
  dist: app + "/static/", // build files
  dist_assets: app + "/static/", //build assets files
};


/*
Copy third party libs
*/

function copyAssets() {
  var out = folder.dist_assets + "/libs/";
  return gulp
    .src(npmdist(), { base: "./node_modules" })
    .pipe(
      rename(function (path) {
        path.dirname = path.dirname.replace(/\/dist/, "").replace(/\\dist/, "");
      })
    )
    .pipe(gulp.dest(out));
}

// image processing
function imageMin() {
  var out = folder.dist_assets + "images";
  return gulp
    .src(folder.src + "images/**/*")
    .pipe(newer(out))
    .pipe(imagemin())
    .pipe(gulp.dest(out));
}

// copy fonts from src folder to dist folder
function fonts() {
  var out = folder.dist_assets + "fonts/";

  return gulp.src([folder.src + "fonts/**/*"]).pipe(gulp.dest(out));
}

// copy dummy data in assets
function data() {
  var out = folder.dist_assets + "data/";

  return gulp.src([folder.src + "data/**/*"]).pipe(gulp.dest(out));
}


// compile & minify sass
function css() {
  gulp
    .src([folder.src + "/scss/**/*.scss"])
    .pipe(sourcemaps.init())
    .pipe(sass()) // scss to css
    .pipe(
      autoprefixer({
        overrideBrowserslist: ["> 1%"],
      })
    )
    .pipe(gulp.dest(folder.dist_assets + "css/"))
    .pipe(cleanCSS())
    .pipe(
      rename({
        // rename app.css to icons.min.css
        suffix: ".min",
      })
    )
    .pipe(sourcemaps.write("./")) // source maps for icons.min.css
    .pipe(gulp.dest(folder.dist_assets + "css/"));

  return gulp
    .src([folder.src + "/scss/**/*.scss"])
    .pipe(sourcemaps.init())
    .pipe(sass()) // scss to css
    .pipe(
      autoprefixer({
        overrideBrowserslist: ["> 1%"],
      })
    )
    .pipe(gulp.dest(folder.dist_assets + "css/"))
    .pipe(rtlcss())
    .pipe(
      rename({
        // rename app.css to icons.min.css
        suffix: "-rtl.min",
      })
    )
    .pipe(sourcemaps.write("./")) // source maps for icons.min.css
    .pipe(gulp.dest(folder.dist_assets + "css/"));
}

// js
function jsPages() {
  var out = folder.dist_assets + "js/";

  return gulp
    .src(folder.src + "src-js/pages/*.js")
    .pipe(uglify())
    .on("error", function (err) {
      console.log(err.toString());
    })
    .pipe(gulp.dest(out + "pages"));
}

function jsVendor() {
  var out = folder.dist_assets + "js/";

  // It's important to keep files at this order
  // so that `app.min.js` can be executed properly
  return gulp
    .src([
      folder.dist_assets + "libs/jquery/jquery.min.js",
      folder.dist_assets + "libs/bootstrap/js/bootstrap.bundle.min.js",
      folder.dist_assets + "libs/simplebar/simplebar.min.js",
      folder.dist_assets + "libs/node-waves/waves.min.js",
      folder.dist_assets + "libs/waypoints/lib/jquery.waypoints.min.js",
      folder.dist_assets + "libs/jquery.counterup/jquery.counterup.min.js",
      folder.dist_assets + "libs/feather-icons/feather.min.js",
    ])
    .pipe(sourcemaps.init())
    .pipe(concat("vendor.js"))
    .pipe(gulp.dest(out))
    .pipe(
      rename({
        // rename app.js to app.min.js
        suffix: ".min",
      })
    )
    .pipe(minify())
    .on("error", function (err) {
      console.log(err.toString());
    })
    .pipe(sourcemaps.write("./"))
    .pipe(gulp.dest(out));
}

function jsTheme() {
  var out = folder.dist_assets + "js/";

  return gulp
    .src([folder.src + "src-js/layout.js", folder.src + "src-js/app.js"])
    .pipe(sourcemaps.init())
    .pipe(concat("bundle.js"))
    .pipe(gulp.dest(out))
    .pipe(
      rename({
        // rename app.js to app.min.js
        suffix: ".min",
      })
    )
    .pipe(uglify())
    .on("error", function (err) {
      console.log(err.toString());
    })
    .pipe(sourcemaps.write("./"))
    .pipe(gulp.dest(out));
}

// watch all changes
function watchFiles() {
  gulp.watch(
    folder.src + "assets/images/**/*",
    gulp.series(imageMin)
  );
  gulp.watch(
    folder.src + "assets/fonts/**/*",
    gulp.series(fonts)
  );
  gulp.watch(folder.src + "scss/**/*", gulp.series(css));
  gulp.watch(folder.src + "js/pages/*.js", jsPages);
  gulp.watch([folder.src + "js/layout.js", folder.src + "js/app.js"], jsTheme);
}

// watch all changes
gulp.task("watch", gulp.parallel(watchFiles));

// default task
gulp.task(
  "default",
  gulp.series(
    copyAssets,
    imageMin,
    fonts,
    data,
    css,
    jsVendor,
    jsPages,
    jsTheme,
    "watch"
  ),
  function (done) {
    done();
  }
);

// build
gulp.task(
  "build",
  gulp.series(
    copyAssets,
    imageMin,
    fonts,
    data,
    css,
    jsVendor,
    jsPages,
    jsTheme
  )
);
