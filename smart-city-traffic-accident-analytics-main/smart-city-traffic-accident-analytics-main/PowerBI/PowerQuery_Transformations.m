/* ==========================================================================
   UrbanFlow Smart City Traffic & Accident Analysis - Power Query M Code
   ETL script for loading and transforming accident data and creating dimensions
   ========================================================================== */

// --------------------------------------------------------------------------
// 1. FACT TABLE: accident_data
// --------------------------------------------------------------------------
let
    // Note: Update path if required or use parameter
    Source = Csv.Document(File.Contents("accident_data.csv"), [Delimiter=",", Columns=24, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{
        {"accident_id", Int64.Type},
        {"city", type text},
        {"state", type text},
        {"latitude", type number},
        {"longitude", type number},
        {"date", type date},
        {"time", type time},
        {"hour", Int64.Type},
        {"day_of_week", type text},
        {"is_weekend", Int64.Type},
        {"road_type", type text},
        {"lanes", Int64.Type},
        {"traffic_signal", Int64.Type},
        {"weather", type text},
        {"visibility", type text},
        {"temperature", type number},
        {"traffic_density", type text},
        {"cause", type text},
        {"accident_severity", type text},
        {"vehicles_involved", Int64.Type},
        {"casualties", Int64.Type},
        {"is_peak_hour", Int64.Type},
        {"festival", type text},
        {"risk_score", type number}
    }),
    #"Replaced Festival Nulls" = Table.ReplaceValue(#"Changed Type", null, "Regular Day", Replacer.ReplaceValue, {"festival"}),
    #"Capitalized Severity" = Table.TransformColumns(#"Replaced Festival Nulls", {{"accident_severity", Text.Proper, type text}}),
    #"Capitalized Weather" = Table.TransformColumns(#"Capitalized Severity", {{"weather", Text.Proper, type text}}),
    #"Capitalized RoadType" = Table.TransformColumns(#"Capitalized Weather", {{"road_type", Text.Proper, type text}}),
    #"Capitalized Cause" = Table.TransformColumns(#"Capitalized RoadType", {{"cause", Text.Proper, type text}}),
    #"Added Severity Weight" = Table.AddColumn(#"Capitalized Cause", "Severity_Weight", each 
        if [accident_severity] = "Fatal" then 5 
        else if [accident_severity] = "Major" then 3 
        else 1, Int64.Type),
    #"Added Risk Tier" = Table.AddColumn(#"Added Severity Weight", "Risk_Tier", each 
        if [risk_score] >= 0.70 then "High Risk" 
        else if [risk_score] >= 0.30 then "Medium Risk" 
        else "Low Risk", type text)
in
    #"Added Risk Tier"


// --------------------------------------------------------------------------
// 2. DIMENSION TABLE: Dim_Calendar (Date Dimension)
// --------------------------------------------------------------------------
let
    StartDate = #date(2022, 1, 1),
    EndDate = #date(2025, 12, 31),
    NumberOfDays = Duration.Days(EndDate - StartDate) + 1,
    DateList = List.Dates(StartDate, NumberOfDays, #duration(1, 0, 0, 0)),
    #"Converted to Table" = Table.FromList(DateList, Splitter.SplitByNothing(), {"Date"}, null, ExtraValues.Error),
    #"Changed Type" = Table.TransformColumnTypes(#"Converted to Table",{{"Date", type date}}),
    #"Inserted Year" = Table.AddColumn(#"Changed Type", "Year", each Date.Year([Date]), Int64.Type),
    #"Inserted Quarter" = Table.AddColumn(#"Inserted Year", "Quarter", each "Q" & Text.From(Date.QuarterOfYear([Date])), type text),
    #"Inserted Month" = Table.AddColumn(#"Inserted Quarter", "MonthNumber", each Date.Month([Date]), Int64.Type),
    #"Inserted Month Name" = Table.AddColumn(#"Inserted Month", "MonthName", each Date.MonthName([Date]), type text),
    #"Inserted Month Short" = Table.AddColumn(#"Inserted Month Name", "MonthShort", each Text.Start([MonthName], 3), type text),
    #"Inserted Day of Week" = Table.AddColumn(#"Inserted Month Short", "DayOfWeek", each Date.DayOfWeekName([Date]), type text),
    #"Inserted Is Weekend" = Table.AddColumn(#"Inserted Day of Week", "IsWeekend", each if Date.DayOfWeek([Date], Day.Monday) >= 5 then 1 else 0, Int64.Type),
    #"Inserted YearMonth" = Table.AddColumn(#"Inserted Is Weekend", "YearMonth", each Text.From([Year]) & "-" & Text.PadStart(Text.From([MonthNumber]), 2, "0"), type text)
in
    #"Inserted YearMonth"
