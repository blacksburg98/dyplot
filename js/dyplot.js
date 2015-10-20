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

