var jwt = sessionStorage.getItem("jwt");
if (jwt == null) {
  window.location.href = "./login.html";
}


$("#menu-toggle").click(function (e) {
  e.preventDefault();
  $("#wrapper").toggleClass("toggled");
});

function logout() {
  sessionStorage.removeItem("jwt");
  window.location.href = "./login.html";
}

const labels = [
  "Post 1",
  "Post 2",
  "Post 3",
  "Post 4",
  "Post 5",
  "Post 6",
  "Post 7",
  "Post 8",
  "Post 9",
  "Post 10",
  "Post 11",
  "Post 12",
];

// var dataLikes = {
//   label: "Likes",
//   data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
//   lineTension: 0,
//   fill: false,
//   borderColor: 'red'
// }

// var dataComments = {
//   label: "Comment",
//   data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
//   lineTension: 0,
//   fill: false,
//   borderColor: 'blue'
// }

const data = {
  labels: labels,
  datasets: [
    {
      label: "Likes",
      lineTension: 0.5,
      pointRadius: 3,
      pointHoverRadius: 3,
      fill: true,
      backgroundColor: "rgba(61, 204, 145, 0.20)",
      borderColor: "rgba(61, 205, 144, 1)",
      data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    },
  ],
};
const data2 = {
  labels: labels,
  datasets: [
    {
      label: "Likes",
      lineTension: 0.5,
      pointRadius: 3,
      pointHoverRadius: 3,
      fill: true,
      backgroundColor: "rgba(61, 204, 145, 0.20)",
      borderColor: "rgba(61, 205, 144, 1)",
      data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    },
  ],
};

const config = {
  type: "line",
  data: data,
  options: {},
};

const configNew ={
  type: "line",
  data: data2,
  options: {},
}

const myChart = new Chart(document.getElementById("myChart"), config);
const myChart2 = new Chart(document.getElementById("myChart2"), configNew)

$(document).ready(function () {
  async function fetchData() {
    var getUsr = document.getElementById("userSearch").innerHTML
    var urlGrade = "../static/assets/json/data-" + getUsr + ".json"
    console.log(urlGrade)
    const url = urlGrade;
    const response = await fetch(url);
    const datapoints = await response.json();
    // console.log(datapoints)
    return datapoints;
  }

  fetchData().then((datapoints) => {
    const post = datapoints.map(function (index) {
      return "Post " + index.id;
    });

    const likes = datapoints.map(function (index) {
      return index.like;
    });

    const comments = datapoints.map(function (index) {
      return index.comment;
    });

    myChart.config.data.labels = post;
    myChart.config.data.datasets[0].data = likes;
    myChart.update();
  });
})

var longText = $("#biography");
longText.text(longText.text().substr(0, 500));

function submitform() {
  document.getElementById("loading").style.display = "block";
  // return false;
  var test = document.getElementById("usernameIg").value;
  document.getElementById("showValue").innerHTML = test;
  console.log(test);
}

// $(document).ready(function($) {
//   $(".table-row").click(function() {
//       alert("success")
//   });
// });

$(document).ready(function () {
  function saveScreenshot(canvas) {
    var downloadLink = document.createElement("a");
    downloadLink.download = "instagram-profile.jpg";
    canvas.toBlob(function (blob) {
      downloadLink.href = URL.createObjectURL(blob);
      downloadLink.click();
    });
  }
  $(".download-btn").on("click", function (e) {
    e.preventDefault();
    html2canvas(document.querySelector(".download-container"), {
      scrollX: 0,
      scrollY: 0,
    }).then(function (canvas) {
      var image = canvas.toDataURL("image/jpeg");
      document.getElementById("created-element").src = image;
      $(this).attr("href", image);
      saveScreenshot(canvas);
    });
  });
});



// Count
$(document).ready(function () {
  async function loadJSON(url) {
    const res = await fetch(url);
    return await res.json();
  }
    var getUsr = document.getElementById("userSearch").innerHTML
  var urlGrade = "../static/assets/json/grade-" + getUsr + ".json"
  loadJSON(urlGrade).then((data) => {
    console.log(data);
    // var nameTest = data[0].name;
    // let followers = data[0].followers;
    // var ER = data[0].ER;
    var followers = data[0].followers;
    var er = data[0].ER;
    let grade;
    let tier;
    if (followers > 1000000) {
      if (er >= 1.97) {
        grade = "A";
      } else if (er >= 1.82 && er < 1.97) {
        grade = "B";
      } else if (er >= 1.67 && er < 1.82) {
        grade = "C";
      } else {
        grade = "D";
      }
    } else if (followers > 100000 && followers <= 1000000) {
      if (er >= 2.05) {
        grade = "A";
      } else if (er >= 1.85 && er < 2.15) {
        grade = "B";
      } else if (er >= 1.65 && er < 1.85) {
        grade = "C";
      } else {
        grade = "D";
      }
    } else if (followers > 20000 && followers <= 100000) {
      if (er >= 2.15) {
        grade = "A";
      } else if (er >= 1.85 && er < 2.15) {
        grade = "B";
      } else if (er >= 1.55 && er < 1.85) {
        grade = "C";
      } else {
        grade = "D";
      }
    } else if (followers > 5000 && followers <= 20000) {
      if (er >= 2.43) {
        grade = "A";
      } else if (er >= 2.0 && er < 2.43) {
        grade = "B";
      } else if (er >= 1.57 && er < 2.0) {
        grade = "C";
      } else {
        grade = "D";
      }
    } else if (followers > 1000 && followers <= 5000) {
      if (er >= 5.6) {
        grade = "A";
      } else if (er >= 4.6 && er < 5.6) {
        grade = "B";
      } else if (er >= 3.6 && er < 4.6) {
        grade = "C";
      } else {
        grade = "D";
      }
    }
    
    if(followers > 1000000){
      tier = "Mega"
    } else if(followers > 500000 && followers <= 1000000){
      tier = "Macro"
    } else if(followers > 50000 && followers <= 500000){
      tier = "Mid Tier"
    } else if(followers > 10000 && followers <= 50000){
      tier = "Micro"
    } else{
      tier = "Nano"
    }

    // console.log(tier)
    document.getElementById("tierInfluencer").innerHTML = tier + " Influencer"
    // document.getElementById("outputtest").innerHTML = grade
    var theLetters = "ABCDEF"; // customize what letters it will cycle through
    var ctnt = grade; // Your text goes here
    var speed = 10; // ms per frame
    var increment = 80; // frames per step. Must be >2
    var clen = ctnt.length;
    var si = 0;
    var stri = 0;
    var block = "";
    var fixed = "";
    //Call self x times, whole function wrapped in setTimeout
    (function rustle(i) {
      setTimeout(function () {
        if (--i) {
          rustle(i);
        }
        nextFrame(i);
        si = si + 1;
      }, speed);
    })(clen * increment + 1);
    function nextFrame(pos) {
      for (var i = 0; i < clen - stri; i++) {
        //Random number
        var num = Math.floor(theLetters.length * Math.random());
        //Get random letter
        var letter = theLetters.charAt(num);
        block = block + letter;
      }
      if (si == increment - 1) {
        stri++;
      }
      if (si == increment) {
        // Add a letter;
        // every speed*10 ms
        fixed = fixed + ctnt.charAt(stri - 1);
        si = 0;
      }
      $("#output-grade").html(fixed + block);
      block = "";
    }
  });
});
