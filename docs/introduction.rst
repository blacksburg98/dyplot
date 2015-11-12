Introduction
============

We can look at the javascript example at `dygraphs.com <http://dygraphs.com>`_.
::
    <script type="text/javascript">
    g = new Dygraph(
    document.getElementById("demodiv"),
            "ny-vs-sf.txt",
            {
            rollPeriod: 14,
            showRoller: true,
            customBars: true,
            title: 'NYC vs. SF',
            ylabel: 'Temperature (F)',
            legend: 'always'
            }
            );
    </script>

For dygraph to work, we need to specify at least three things in html code.

1. *g*: the javascript variable of the Dygraph object
2. *demodiv*: The div id. dygraph will draw the chart on this part of the page.
3. *ny-vs-sf.txt*: The url path to the data file.

We can use the following python codes to generate a random array and plot
it with dyplot.
::
        import numpy as np
        import pandas as pd
        from dyplot.dygraphs import Dygraphs
        if __name__ == '__main__':
            foo = np.random.rand(100)
            boo = pd.Series(foo, index=range(0,100))
            dg = Dygraphs(boo.index, "date") 
            dg.plot(series="Random", mseries=boo)
            dg.set_options(title="Tutorial 0")
            div = dg.savefig(csv_file="tutorial0.csv", div_id="demodiv", js_vid="jid", html_file="tutorial0.html")

dg.savefig return the html codes to be embedded in html and save html codes to tutorial0.html.
The content of div is:
::
    
    <div id="demodiv" style="width:1024px; height:600px;"></div>
    <script type="text/javascript">
    jid = new Dygraph(
        document.getElementById("demodiv"),
        "tutorial0.csv", // path to CSV file
    {"legend": "always", "series": {"Random": {"axis": "y"}}, "showRoller": false, "ylabel": "Y Values", "title": "Tutorial 0", "customBars": true, "axes": {"x": {}, "y": {"valueRange": [0.025494957864579806, 1.0853730685966185]}, "y2": {"valueRange": []}}}  );
      jid.ready(function() {
        jid.setAnnotations([]    );
      });
    </script>

You can see the `output <http://blacksburg98.github.io/dyplot/html/tutorial0.html>`_. 
