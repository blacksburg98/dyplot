function candlePlotter(e) {
  var BAR_WIDTH = 8;
  // This is the officially endorsed way to plot all the series at once.
  if (e.seriesIndex !== 0) return;

  var setCount = e.seriesCount;
  if (setCount < 4) {
    throw "More than 4 prices each point must be provided. The first 4 prices are used for Candlestick.";
  }
  var prices = [];
  var price;
  var sets = e.allSeriesPoints;
  for (var p = 0 ; p < sets[0].length; p++) {
    price = {
      open : sets[0][p].yval,
      high : sets[1][p].yval,
      low : sets[2][p].yval,
      close : sets[3][p].yval,
      openY : sets[0][p].y,
      highY : sets[1][p].y,
      lowY : sets[2][p].y,
      closeY : sets[3][p].y
    };
    prices.push(price);
  }

  var area = e.plotArea;
  var ctx = e.drawingContext;
  ctx.strokeStyle = '#202020';
  ctx.lineWidth = 0.6;

  for (p = 0 ; p < prices.length; p++) {
    ctx.beginPath();

    price = prices[p];
    var topY = area.h * price.highY + area.y;
    var bottomY = area.h * price.lowY + area.y;
    var centerX = area.x + sets[0][p].x * area.w;
    ctx.moveTo(centerX, topY);
    ctx.lineTo(centerX, bottomY);
    ctx.closePath();
    ctx.stroke();
    var bodyY;
    if (price.open > price.close) {
      ctx.fillStyle ='rgba(244,44,44,1.0)';
      bodyY = area.h * price.openY + area.y;
    }
    else {
      ctx.fillStyle ='rgba(44,244,44,1.0)';
      bodyY = area.h * price.closeY  + area.y;
    }
    var bodyHeight = area.h * Math.abs(price.openY - price.closeY);
    ctx.fillRect(centerX - BAR_WIDTH / 2, bodyY, BAR_WIDTH,  bodyHeight);
  }
  var g = e.dygraph;
  var colors = g.getColors();
  for (var c = 4; c < setCount; c++) {
    for (var p = 1 ; p < sets[c].length; p++) {
      ctx.strokeStyle = colors[c];
      var Y0 = area.h * sets[c][p-1].y + area.y;
      var Y1 = area.h * sets[c][p].y + area.y;
      var X0 = area.x + sets[c][p-1].x * area.w;
      var X1 = area.x + sets[c][p].x * area.w;
      ctx.beginPath();
      ctx.moveTo(X0, Y0);
      ctx.lineTo(X1, Y1);
      ctx.closePath();
      ctx.stroke();
    }
  }
}

// This function draws bars for a single series. See
// multiColumnBarPlotter below for a plotter which can draw multi-series
// bar charts.
function barChartPlotter(e) {
  var ctx = e.drawingContext;
  var points = e.points;
  var y_bottom = e.dygraph.toDomYCoord(0);

  ctx.fillStyle = darkenColor(e.color);

  // Find the minimum separation between x-values.
  // This determines the bar width.
  var min_sep = Infinity;
  for (var i = 1; i < points.length; i++) {
    var sep = points[i].canvasx - points[i - 1].canvasx;
    if (sep < min_sep) min_sep = sep;
  }
  var bar_width = Math.floor(2.0 / 3 * min_sep);

  // Do the actual plotting.
  for (var i = 0; i < points.length; i++) {
    var p = points[i];
    var center_x = p.canvasx;

    ctx.fillRect(center_x - bar_width / 2, p.canvasy,
        bar_width, y_bottom - p.canvasy);

    ctx.strokeRect(center_x - bar_width / 2, p.canvasy,
        bar_width, y_bottom - p.canvasy);
  }
}
function setStatus() {
  document.getElementById("visibility").innerHTML =
          g.visibility().toString();
}
function change(el) {
  g.setVisibility(parseInt(el.id), el.checked);
  setStatus();
}
// Scatter function
// use nvd3
function Scatter(chart_data_obj, div, option) {
    final_option = {
        showDistX: true,
        showDistY: true,
        transitionDuration: 350,
        xtickformat: '.02f',
        ytickformat: '.02f',
        onlyCricles: false
      };
    for (var key in option) {
      final_option[key] = option[key] 
    }
    var chart = nv.models.scatterChart()
                  .showDistX(final_option["showDistX"])    //showDist, when true, will display those little distribution lines on the axis.
                  .showDistY(final_option["showDistY"])
                  .transitionDuration(final_option["transitionDuration"])
                  .color(d3.scale.category10().range());
    //Configure how the tooltip looks.
    chart.tooltipContent(function(key) {
        return '<h3>' + key + '</h3>';
    });
    //Axis settings
    chart.xAxis.tickFormat(d3.format(final_option["xtickformat"]));
    chart.yAxis.tickFormat(d3.format(final_option["ytickformat"]));
    //We want to show shapes other than circles.
    chart.scatter.onlyCircles(final_option["onlyCircles"]);
    //var myData = randomData(2,40);
    var myData = chart_data_obj
    var div_select = "#".concat(div).concat(" svg")
    d3.select(div_select)
        .datum(myData)
        .call(chart);
    nv.utils.windowResize(chart.update);
    return chart;
}
function scatter_chart(arg) {
  $.ajax({
      type: "GET",
      url: arg["chart_data"],
      dataType: "text",
      success: function(data) {
          var csv_data;
          var chart_data_obj = [];
          d = data.replace(/\r\n|\r/gm, "\n");
          csv_data = d.split("\n");
          csv_data.pop();
          var head = csv_data[0]
          var groups = head.split(",")
          for(i = 0; i < groups.length; i++) {
              chart_data_obj.push({
                  key: groups[i],
                  values: []
              });
          }
          for(j = 1; j < csv_data.length; j++) {
              g = csv_data[j].split(",");
              for(k = 0; k < g.length; k++) {
                  items = g[k].split(";");
                  var size = 1;
                  var shape = "circle";
                  if(items[2] != "") size = items[2];
                  if(items[3] != "") shape = items[3];
                  chart_data_obj[k].values.push({
                      x: items[0],
                      y: items[1],
                      size: size,
                      shape: shape
                  });
              }
          }
          nv.addGraph(Scatter(chart_data_obj,arg["div"], arg["option"]));
      }
  });
}
