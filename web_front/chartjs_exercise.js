window.chartColors = {
  red: "#FF0000",
  blue: "#00FF00"
};

var color = Chart.helpers.color;
var scatter_data = {
  datasets:[{
    label: "schatter dots",
    borderColor: window.chartColors.red,
    backgroundColor: color(window.chartColors.red).alpha(0.2).rgbString(),
    pointRadius: 10,

    data: [{
      x: 20.3,
      y: 13.43
    },{
      x: 17.9,
      y: 4.2
    },{
      x: 10.9,
      y: 15.2
      // x: 1/randomScalingFactor(),
      // y: 1/randomScalingFactor()
    }]

  }]
};

var ctx = document.getElementById('canvas').getContext('2d');
window.myScatter = Chart.Scatter(ctx, {
// var scatter_chart = new Chart(ctx, 
  data: scatter_data,
  option:{
    title: {
      display: true,
      text: "Chart.js Scatter Chart"
    },
  }
});

