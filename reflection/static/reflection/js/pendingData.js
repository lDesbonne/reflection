var width = 480,
    height = 350,
    radius = (Math.min(width, height) / 2) - 10;

var formatNumber = d3.format(",d");

var x = d3.scaleLinear()
    .range([0, 2 * Math.PI]);

var y = d3.scaleSqrt()
    .range([0, radius]);

var color = d3.scaleOrdinal(d3.schemeCategory20);

var partition = d3.partition();

var arc = d3.arc()
    .startAngle(function(d) { return Math.max(0, Math.min(2 * Math.PI, x(d.x0))); })
    .endAngle(function(d) { return Math.max(0, Math.min(2 * Math.PI, x(d.x1))); })
    .innerRadius(function(d) { return Math.max(0, y(d.y0)); })
    .outerRadius(function(d) { return Math.max(0, y(d.y1)); });


var pendingChart = d3.select("#PendingData").append("svg")
    .attr("width", width)
    .attr("height", height)
  .append("g")
    .attr("transform", "translate(" + width / 2 + "," + (height / 2) + ")")
    .attr("align","right");

(function() {
  var root = d3.hierarchy(dormantData);	
  root.sum(function(d) { return d.size; });
  pendingChart.selectAll("path")
      .data(partition(root).descendants())
    .enter().append("path")
      .attr("d", arc)
      .style("fill", function(d) { return color((d.children ? d : d.parent).data.name); })
      .on("click", clickPendingChart)
      .append("title")
      .text(function(d) { return d.data.name})
      .style("font-size", "8px");
})();

function clickPendingChart(d) {
	if (d.data.detail != "root" && d.data.select != "False") {
		document.getElementById("searchData").value = d.data.name;
		if (d.data.detail) {
			document.getElementById("information").innerHTML = d.data.detail;
		} else {
			document.getElementById("information").innerHTML = "No Information";
		}
		updateData.id = d.data.id;
		updateData.status = "T";
		if (d.hasOwnProperty('children')) {
			updateData.type = 'Topic';
		} else {
			updateData.type = 'Question';
		}
		document.getElementById("activate").disabled = false;
		document.getElementById("deactivate").disabled = true;
	}
  
  pendingChart.transition()
      .duration(750)
      .tween("scale", function() {
        var xd = d3.interpolate(x.domain(), [d.x0, d.x1]),
            yd = d3.interpolate(y.domain(), [d.y0, 1]),
            yr = d3.interpolate(y.range(), [d.y0 ? 20 : 0, radius]);
        return function(t) { x.domain(xd(t)); y.domain(yd(t)).range(yr(t)); };
      })
    .selectAll("path")
      .attrTween("d", function(d) { return function() { return arc(d); }; });
}

d3.select(self.frameElement).style("height", height + "px");