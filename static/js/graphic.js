var recipes = $('#charts-container').data('recipes');
makeGraphs(recipes);
  
function makeGraphs(data) {
    var cookingTimeBarChart = dc.barChart('#cooking-time-chart');
    var preparationTimeBarChart = dc.barChart('#preparation-time-chart');
    var authorsBarChart = dc.barChart('#authors-chart');
    var celiacsPieChart = dc.pieChart('#celiacs-chart');
    var gluttenFreePieChart = dc.pieChart('#glutten-free-chart');

    const GLUTEN_FREE = 'gluten_free';
    const PREDOMINANT_GROUP = 'predominant_group'; // predominant_group
    const COUSINE_NAME = 'cuisine_name';
    const COOKING_TIME = 'cooking_time'; //: "350",
    const PREPARATION_FOOD = 'preparation_food'; //: "125"
    const AUTHOR_NAME = 'author_name';
    
    
    console.log(data)

    var ndx = crossfilter(data);
    var cousineNameDimension = ndx.dimension((d) => d[COUSINE_NAME]);
    var preparationSumGroup = cousineNameDimension.group().reduceSum((d) => d[COOKING_TIME]);
    var preparationGroup = cousineNameDimension.group().reduceSum((d) => d[PREPARATION_FOOD]);
    var cuisineGroup = cousineNameDimension.group();
    var foodgroupname = ndx.dimension((d) => d[PREDOMINANT_GROUP]);
    var foodGroup = foodgroupname.group();
    var authorname = ndx.dimension((d) => d[AUTHOR_NAME]);
    var authorGroup = authorname.group();
    
    var resetButton = $('#reset-filter-button');
    resetButton.on('click', function(event) {
        dc.filterAll();
        dc.renderAll();
    });

    // console.log(preparationSumGroup.all());
    
    cookingTimeBarChart
        .width(528)
        .height(450)
        .x(d3.scaleBand())
        .xUnits(dc.units.ordinal)
        .brushOn(false)
        .xAxisLabel(COUSINE_NAME)
        .yAxisLabel("time for cooking(min)")
        .dimension(cousineNameDimension)
        .transitionDuration(500)
        .barPadding(0.1)
        .outerPadding(0.05)
        .group(preparationSumGroup).elasticY();
        
        
    // console.log(preparationSumGroup.all());

    preparationTimeBarChart
        .width(528)
        .height(450)
        .x(d3.scaleBand())
        .xUnits(dc.units.ordinal)
        .brushOn(false)
        .xAxisLabel(PREPARATION_FOOD)
        .yAxisLabel("time for prep(min)")
        .dimension(cousineNameDimension)
        .barPadding(0.1)
        .outerPadding(0.5)
        .group(preparationGroup)
        .renderHorizontalGridLines(true)
            .on('renderlet',function(chart){
                  chart.selectAll("g.x text")
                    .attr('dx', '-15')
                    .attr('transform', "rotate(-20)");
                });
         
    // console.log(preparationSumGroup.all());

    authorsBarChart
        .width(528)
        .height(480)
        .x(d3.scaleBand())
        .xUnits(dc.units.ordinal)
        .brushOn(true)
        .xAxisLabel(COUSINE_NAME)
        .yAxisLabel("number of cuisine")
        .dimension(cousineNameDimension)
        .transitionDuration(500)
        .barPadding(0.1)
        .outerPadding(0.05)
        .group(cuisineGroup)
        .renderHorizontalGridLines(true)
            .on('renderlet',function(chart){
                  chart.selectAll("g.x text")
                    .attr('dx', '-15')
                    .attr('transform', "rotate(-20)");
                });
        
    // console.log(preparationSumGroup.all());
    
    celiacsPieChart
        .width(368)
        .radius(90)
        .transitionDuration(1500)
        .dimension(foodgroupname)
        .group(foodGroup)
        .legend(dc.legend().x(290).y(10).itemHeight(8).gap(3) ); 
        
    // console.log(preparationSumGroup.all());

    gluttenFreePieChart
        .width(368)
        .radius(90)
        .transitionDuration(1500)
        .dimension(authorname)
        .group(authorGroup)
        .legend(dc.legend().x(290).y(10).itemHeight(8).gap(3) ); 
    
    dc.renderAll();
    // console.log(preparationSumGroup.all());
}

