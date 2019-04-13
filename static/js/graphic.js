function makeGraphs(data) {
    var commitmentByProgrammeNameChart = dc.barChart('#first-graph');
    var commitmentByProgrammeNameChart1 = dc.barChart('#first-graph1');
    var commitmentByProgrammeNameChart2 = dc.barChart('#first-graph2');
    var commitmentByProgrammeNameChart3 = dc.pieChart('#first-graph3');
    var commitmentByProgrammeNameChart4 = dc.pieChart('#first-graph4');



    const GLUTEN_FREE = 'gluten_free';
    const PREDOMINANT_GROUP = 'predominant_group'; // predominant_group
    const COUSINE_NAME = 'cuisine_name';
    const COOKING_TIME = 'cooking_time'; //: "350",
    const PREPARATION_FOOD = 'preparation_food'; //: "125"
    const AUTHOR_NAME = 'author_name';

    // var parseDate = d3.timeParse("%d/%m/%Y");

    data.forEach((d) => {
        d[COOKING_TIME] = Number(d[COOKING_TIME]);
        d[PREPARATION_FOOD] = Number(d[PREPARATION_FOOD]);
    });

    var ndx = crossfilter(data);
    var cousineNameDimension = ndx.dimension((d) => d[COUSINE_NAME]);
    var preparationSumGroup = cousineNameDimension.group().reduceSum((d) => d[COOKING_TIME]);

    console.log(preparationSumGroup.all());

    commitmentByProgrammeNameChart
        .width(768)
        .height(480)
        .x(d3.scaleBand())
        .xUnits(dc.units.ordinal)
        .brushOn(false)
        .xAxisLabel(COUSINE_NAME)
        .yAxisLabel("time for cooking(min)")
        .dimension(cousineNameDimension)
        .barPadding(0.1)
        .outerPadding(0.05)
        .group(preparationSumGroup);

    commitmentByProgrammeNameChart.render();


    var ndx = crossfilter(data);
    var PrepNameDimension = ndx.dimension((d) => d[COUSINE_NAME]);
    var preparationGroup = cousineNameDimension.group().reduceSum((d) => d[PREPARATION_FOOD]);


    console.log(preparationSumGroup.all());

    commitmentByProgrammeNameChart1
        .width(768)
        .height(480)
        .x(d3.scaleBand())
        .xUnits(dc.units.ordinal)
        .brushOn(false)
        .xAxisLabel(PREPARATION_FOOD)
        .yAxisLabel("time for prep(min)")
        .dimension(PrepNameDimension)
        .barPadding(0.1)
        .outerPadding(0.05)
        .group(preparationGroup);

    commitmentByProgrammeNameChart1.render();
    
    
    var ndx = crossfilter(data);
    var cuisinename = ndx.dimension((d) => d[COUSINE_NAME]);
    var cuisineGroup = cuisinename.group();


    console.log(preparationSumGroup.all());

    commitmentByProgrammeNameChart2
        .width(768)
        .height(480)
        .x(d3.scaleBand())
        .xUnits(dc.units.ordinal)
        .brushOn(true)
        .xAxisLabel(COUSINE_NAME)
        .yAxisLabel("number of cuisine")
        .dimension(cuisinename)
        .barPadding(0.1)
        .outerPadding(0.05)
        .group(cuisineGroup);

    commitmentByProgrammeNameChart2.render();
    
    
    
    var ndx = crossfilter(data);
    var foodgroupname = ndx.dimension((d) => d[PREDOMINANT_GROUP]);
    var foodGroup = foodgroupname.group();


    console.log(preparationSumGroup.all());

    commitmentByProgrammeNameChart3
        .width(368)
        .radius(90)
        .transitionDuration(1500)
        .dimension(foodgroupname)
        .group(foodGroup);

    commitmentByProgrammeNameChart3.render();
    
    

    console.log(preparationSumGroup.all());

    
    var ndx = crossfilter(data);
    var authorname = ndx.dimension((d) => d[AUTHOR_NAME]);
    var authorGroup = authorname.group();


    console.log(preparationSumGroup.all());

    commitmentByProgrammeNameChart4
        .width(368)
        .radius(90)
        .transitionDuration(1500)
        .dimension(authorname)
        .group(authorGroup)
        .legend(dc.legend().x(420).y(0).itemHeight(155).gap(5) ); 

    commitmentByProgrammeNameChart4.render();
    
    

    console.log(preparationSumGroup.all());

     
    
}

