function makeGraphs(data) {
    var commitmentByProgrammeNameChart = dc.barChart('#first-graph');
    
    const GLUTEN_FREE = 'gluten_free';
    // predominant_group
    const COUSINE_NAME = 'cuisine_name';
    // author_name
    const COOKING_TIME = 'cooking_time'; //: "350",
    const PREPARATION_FOOD = 'preparation_food'; //: "125"

    // var parseDate = d3.timeParse("%d/%m/%Y");
  
    data.forEach((d) => {
        d[COOKING_TIME] = Number(d[COOKING_TIME]);
        d[PREPARATION_FOOD] = Number(d[PREPARATION_FOOD]);
    });
    
    var ndx = crossfilter(data);
    var cousineNameDimension = ndx.dimension((d) => d[COUSINE_NAME]);
    var preparationSumGroup = cousineNameDimension.group().reduceSum((d) => d[PREPARATION_FOOD]);
    
    console.log(preparationSumGroup.all());
    
    commitmentByProgrammeNameChart
        .width(768)
        .height(480)
        .x(d3.scaleBand())
        .xUnits(dc.units.ordinal)
        .brushOn(false)
        .xAxisLabel(COUSINE_NAME)
        .yAxisLabel("time for preparing(min)")
        .dimension(cousineNameDimension)
        .barPadding(0.1)
        .outerPadding(0.05)
        .group(preparationSumGroup);

    commitmentByProgrammeNameChart.render();
}