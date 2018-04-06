from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Vister_td(User):
    name = models.CharField(max_length=12, null=False, default='')
    carNum = models.CharField(max_length=12, null=False, default='')
    carType = models.CharField(max_length=20, null=False, default='')
    regTime = models.CharField(max_length=25, null=False, default='')

    def __str__(self):
        return self.name


class Car_td(models.Model):
   # id = models.IntegerField(primary_key=True)  # AutoField?
    carnum = models.CharField(db_column='carNum', max_length=12)  # Field name made lowercase.
    area = models.CharField(max_length=20)
    entertime_year = models.IntegerField(db_column='enterTime_Year')  # Field name made lowercase.
    entertime_month = models.IntegerField(db_column='enterTime_Month')  # Field name made lowercase.
    entertime_day = models.IntegerField(db_column='enterTime_Day')  # Field name made lowercase.
    entertime_time = models.IntegerField(db_column='enterTime_Time')  # Field name made lowercase.
    leavetime_year = models.IntegerField(db_column='leaveTime_Year')  # Field name made lowercase.
    leavetime_month = models.IntegerField(db_column='leaveTime_Month')  # Field name made lowercase.
    leavetime_day = models.IntegerField(db_column='leaveTime_Day')  # Field name made lowercase.
    leavetime_time = models.IntegerField(db_column='leaveTime_Time')  # Field name made lowercase.
    note = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cars_car_td'

    def __str__(self):
        return self.carnum


class admin_td(models.Model):
    name = models.CharField(max_length=20, null=False, default='')
    pwd = models.CharField(max_length=25, null=False, default='')
    tel = models.CharField(max_length=12, null=False, default='')

    def __str__(self):
        return self.name


class carareanum(models.Model):
    #id = models.IntegerField(primary_key=True)
    totalnum = models.IntegerField()
    remainingnum = models.IntegerField()

class CardataApril(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    day1 = models.IntegerField(db_column='Day1', blank=True, null=True)  # Field name made lowercase.
    day2 = models.IntegerField(db_column='Day2', blank=True, null=True)  # Field name made lowercase.
    day3 = models.IntegerField(db_column='Day3', blank=True, null=True)  # Field name made lowercase.
    day4 = models.IntegerField(db_column='Day4', blank=True, null=True)  # Field name made lowercase.
    day5 = models.IntegerField(db_column='Day5', blank=True, null=True)  # Field name made lowercase.
    day6 = models.IntegerField(db_column='Day6', blank=True, null=True)  # Field name made lowercase.
    day7 = models.IntegerField(db_column='Day7', blank=True, null=True)  # Field name made lowercase.
    day8 = models.IntegerField(db_column='Day8', blank=True, null=True)  # Field name made lowercase.
    day9 = models.IntegerField(db_column='Day9', blank=True, null=True)  # Field name made lowercase.
    day10 = models.IntegerField(db_column='Day10', blank=True, null=True)  # Field name made lowercase.
    day11 = models.IntegerField(db_column='Day11', blank=True, null=True)  # Field name made lowercase.
    day12 = models.IntegerField(db_column='Day12', blank=True, null=True)  # Field name made lowercase.
    day13 = models.IntegerField(db_column='Day13', blank=True, null=True)  # Field name made lowercase.
    day14 = models.IntegerField(db_column='Day14', blank=True, null=True)  # Field name made lowercase.
    day15 = models.IntegerField(db_column='Day15', blank=True, null=True)  # Field name made lowercase.
    day16 = models.IntegerField(db_column='Day16', blank=True, null=True)  # Field name made lowercase.
    day17 = models.IntegerField(db_column='Day17', blank=True, null=True)  # Field name made lowercase.
    day18 = models.IntegerField(db_column='Day18', blank=True, null=True)  # Field name made lowercase.
    day19 = models.IntegerField(db_column='Day19', blank=True, null=True)  # Field name made lowercase.
    day20 = models.IntegerField(db_column='Day20', blank=True, null=True)  # Field name made lowercase.
    day21 = models.IntegerField(db_column='Day21', blank=True, null=True)  # Field name made lowercase.
    day22 = models.IntegerField(db_column='Day22', blank=True, null=True)  # Field name made lowercase.
    day23 = models.IntegerField(db_column='Day23', blank=True, null=True)  # Field name made lowercase.
    day24 = models.IntegerField(db_column='Day24', blank=True, null=True)  # Field name made lowercase.
    day25 = models.IntegerField(db_column='Day25', blank=True, null=True)  # Field name made lowercase.
    day26 = models.IntegerField(db_column='Day26', blank=True, null=True)  # Field name made lowercase.
    day27 = models.IntegerField(db_column='Day27', blank=True, null=True)  # Field name made lowercase.
    day28 = models.IntegerField(db_column='Day28', blank=True, null=True)  # Field name made lowercase.
    day29 = models.IntegerField(db_column='Day29', blank=True, null=True)  # Field name made lowercase.
    day30 = models.IntegerField(db_column='Day30', blank=True, null=True)  # Field name made lowercase.
    day31 = models.IntegerField(db_column='Day31', blank=True, null=True)  # Field name made lowercase.
    aprilmonthdata = models.IntegerField(db_column='AprilMonthData', blank=True, null=True)  # Field name made lowercase.
    panduan = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'carData_April'


class CardataAugust(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    day1 = models.IntegerField(db_column='Day1', blank=True, null=True)  # Field name made lowercase.
    day2 = models.IntegerField(db_column='Day2', blank=True, null=True)  # Field name made lowercase.
    day3 = models.IntegerField(db_column='Day3', blank=True, null=True)  # Field name made lowercase.
    day4 = models.IntegerField(db_column='Day4', blank=True, null=True)  # Field name made lowercase.
    day5 = models.IntegerField(db_column='Day5', blank=True, null=True)  # Field name made lowercase.
    day6 = models.IntegerField(db_column='Day6', blank=True, null=True)  # Field name made lowercase.
    day7 = models.IntegerField(db_column='Day7', blank=True, null=True)  # Field name made lowercase.
    day8 = models.IntegerField(db_column='Day8', blank=True, null=True)  # Field name made lowercase.
    day9 = models.IntegerField(db_column='Day9', blank=True, null=True)  # Field name made lowercase.
    day10 = models.IntegerField(db_column='Day10', blank=True, null=True)  # Field name made lowercase.
    day11 = models.IntegerField(db_column='Day11', blank=True, null=True)  # Field name made lowercase.
    day12 = models.IntegerField(db_column='Day12', blank=True, null=True)  # Field name made lowercase.
    day13 = models.IntegerField(db_column='Day13', blank=True, null=True)  # Field name made lowercase.
    day14 = models.IntegerField(db_column='Day14', blank=True, null=True)  # Field name made lowercase.
    day15 = models.IntegerField(db_column='Day15', blank=True, null=True)  # Field name made lowercase.
    day16 = models.IntegerField(db_column='Day16', blank=True, null=True)  # Field name made lowercase.
    day17 = models.IntegerField(db_column='Day17', blank=True, null=True)  # Field name made lowercase.
    day18 = models.IntegerField(db_column='Day18', blank=True, null=True)  # Field name made lowercase.
    day19 = models.IntegerField(db_column='Day19', blank=True, null=True)  # Field name made lowercase.
    day20 = models.IntegerField(db_column='Day20', blank=True, null=True)  # Field name made lowercase.
    day21 = models.IntegerField(db_column='Day21', blank=True, null=True)  # Field name made lowercase.
    day22 = models.IntegerField(db_column='Day22', blank=True, null=True)  # Field name made lowercase.
    day23 = models.IntegerField(db_column='Day23', blank=True, null=True)  # Field name made lowercase.
    day24 = models.IntegerField(db_column='Day24', blank=True, null=True)  # Field name made lowercase.
    day25 = models.IntegerField(db_column='Day25', blank=True, null=True)  # Field name made lowercase.
    day26 = models.IntegerField(db_column='Day26', blank=True, null=True)  # Field name made lowercase.
    day27 = models.IntegerField(db_column='Day27', blank=True, null=True)  # Field name made lowercase.
    day28 = models.IntegerField(db_column='Day28', blank=True, null=True)  # Field name made lowercase.
    day29 = models.IntegerField(db_column='Day29', blank=True, null=True)  # Field name made lowercase.
    day30 = models.IntegerField(db_column='Day30', blank=True, null=True)  # Field name made lowercase.
    day31 = models.IntegerField(db_column='Day31', blank=True, null=True)  # Field name made lowercase.
    augustmonthdata = models.IntegerField(db_column='AugustMonthData', blank=True, null=True)  # Field name made lowercase.
    panduan = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'carData_August'


class CardataDecember(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    day1 = models.IntegerField(db_column='Day1', blank=True, null=True)  # Field name made lowercase.
    day2 = models.IntegerField(db_column='Day2', blank=True, null=True)  # Field name made lowercase.
    day3 = models.IntegerField(db_column='Day3', blank=True, null=True)  # Field name made lowercase.
    day4 = models.IntegerField(db_column='Day4', blank=True, null=True)  # Field name made lowercase.
    day5 = models.IntegerField(db_column='Day5', blank=True, null=True)  # Field name made lowercase.
    day6 = models.IntegerField(db_column='Day6', blank=True, null=True)  # Field name made lowercase.
    day7 = models.IntegerField(db_column='Day7', blank=True, null=True)  # Field name made lowercase.
    day8 = models.IntegerField(db_column='Day8', blank=True, null=True)  # Field name made lowercase.
    day9 = models.IntegerField(db_column='Day9', blank=True, null=True)  # Field name made lowercase.
    day10 = models.IntegerField(db_column='Day10', blank=True, null=True)  # Field name made lowercase.
    day11 = models.IntegerField(db_column='Day11', blank=True, null=True)  # Field name made lowercase.
    day12 = models.IntegerField(db_column='Day12', blank=True, null=True)  # Field name made lowercase.
    day13 = models.IntegerField(db_column='Day13', blank=True, null=True)  # Field name made lowercase.
    day14 = models.IntegerField(db_column='Day14', blank=True, null=True)  # Field name made lowercase.
    day15 = models.IntegerField(db_column='Day15', blank=True, null=True)  # Field name made lowercase.
    day16 = models.IntegerField(db_column='Day16', blank=True, null=True)  # Field name made lowercase.
    day17 = models.IntegerField(db_column='Day17', blank=True, null=True)  # Field name made lowercase.
    day18 = models.IntegerField(db_column='Day18', blank=True, null=True)  # Field name made lowercase.
    day19 = models.IntegerField(db_column='Day19', blank=True, null=True)  # Field name made lowercase.
    day20 = models.IntegerField(db_column='Day20', blank=True, null=True)  # Field name made lowercase.
    day21 = models.IntegerField(db_column='Day21', blank=True, null=True)  # Field name made lowercase.
    day22 = models.IntegerField(db_column='Day22', blank=True, null=True)  # Field name made lowercase.
    day23 = models.IntegerField(db_column='Day23', blank=True, null=True)  # Field name made lowercase.
    day24 = models.IntegerField(db_column='Day24', blank=True, null=True)  # Field name made lowercase.
    day25 = models.IntegerField(db_column='Day25', blank=True, null=True)  # Field name made lowercase.
    day26 = models.IntegerField(db_column='Day26', blank=True, null=True)  # Field name made lowercase.
    day27 = models.IntegerField(db_column='Day27', blank=True, null=True)  # Field name made lowercase.
    day28 = models.IntegerField(db_column='Day28', blank=True, null=True)  # Field name made lowercase.
    day29 = models.IntegerField(db_column='Day29', blank=True, null=True)  # Field name made lowercase.
    day30 = models.IntegerField(db_column='Day30', blank=True, null=True)  # Field name made lowercase.
    day31 = models.IntegerField(db_column='Day31', blank=True, null=True)  # Field name made lowercase.
    decembermonthdata = models.IntegerField(db_column='DecemberMonthData', blank=True, null=True)  # Field name made lowercase.
    panduan = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'carData_December'


class CardataFebruary(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    day1 = models.IntegerField(db_column='Day1', blank=True, null=True)  # Field name made lowercase.
    day2 = models.IntegerField(db_column='Day2', blank=True, null=True)  # Field name made lowercase.
    day3 = models.IntegerField(db_column='Day3', blank=True, null=True)  # Field name made lowercase.
    day4 = models.IntegerField(db_column='Day4', blank=True, null=True)  # Field name made lowercase.
    day5 = models.IntegerField(db_column='Day5', blank=True, null=True)  # Field name made lowercase.
    day6 = models.IntegerField(db_column='Day6', blank=True, null=True)  # Field name made lowercase.
    day7 = models.IntegerField(db_column='Day7', blank=True, null=True)  # Field name made lowercase.
    day8 = models.IntegerField(db_column='Day8', blank=True, null=True)  # Field name made lowercase.
    day9 = models.IntegerField(db_column='Day9', blank=True, null=True)  # Field name made lowercase.
    day10 = models.IntegerField(db_column='Day10', blank=True, null=True)  # Field name made lowercase.
    day11 = models.IntegerField(db_column='Day11', blank=True, null=True)  # Field name made lowercase.
    day12 = models.IntegerField(db_column='Day12', blank=True, null=True)  # Field name made lowercase.
    day13 = models.IntegerField(db_column='Day13', blank=True, null=True)  # Field name made lowercase.
    day14 = models.IntegerField(db_column='Day14', blank=True, null=True)  # Field name made lowercase.
    day15 = models.IntegerField(db_column='Day15', blank=True, null=True)  # Field name made lowercase.
    day16 = models.IntegerField(db_column='Day16', blank=True, null=True)  # Field name made lowercase.
    day17 = models.IntegerField(db_column='Day17', blank=True, null=True)  # Field name made lowercase.
    day18 = models.IntegerField(db_column='Day18', blank=True, null=True)  # Field name made lowercase.
    day19 = models.IntegerField(db_column='Day19', blank=True, null=True)  # Field name made lowercase.
    day20 = models.IntegerField(db_column='Day20', blank=True, null=True)  # Field name made lowercase.
    day21 = models.IntegerField(db_column='Day21', blank=True, null=True)  # Field name made lowercase.
    day22 = models.IntegerField(db_column='Day22', blank=True, null=True)  # Field name made lowercase.
    day23 = models.IntegerField(db_column='Day23', blank=True, null=True)  # Field name made lowercase.
    day24 = models.IntegerField(db_column='Day24', blank=True, null=True)  # Field name made lowercase.
    day25 = models.IntegerField(db_column='Day25', blank=True, null=True)  # Field name made lowercase.
    day26 = models.IntegerField(db_column='Day26', blank=True, null=True)  # Field name made lowercase.
    day27 = models.IntegerField(db_column='Day27', blank=True, null=True)  # Field name made lowercase.
    day28 = models.IntegerField(db_column='Day28', blank=True, null=True)  # Field name made lowercase.
    day29 = models.IntegerField(db_column='Day29', blank=True, null=True)  # Field name made lowercase.
    day30 = models.IntegerField(db_column='Day30', blank=True, null=True)  # Field name made lowercase.
    day31 = models.IntegerField(db_column='Day31', blank=True, null=True)  # Field name made lowercase.
    februarymonthdata = models.IntegerField(db_column='FebruaryMonthData', blank=True, null=True)  # Field name made lowercase.
    panduan = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'carData_February'


class CardataJanuary(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    day1 = models.IntegerField(db_column='Day1', blank=True, null=True)  # Field name made lowercase.
    day2 = models.IntegerField(db_column='Day2', blank=True, null=True)  # Field name made lowercase.
    day3 = models.IntegerField(db_column='Day3', blank=True, null=True)  # Field name made lowercase.
    day4 = models.IntegerField(db_column='Day4', blank=True, null=True)  # Field name made lowercase.
    day5 = models.IntegerField(db_column='Day5', blank=True, null=True)  # Field name made lowercase.
    day6 = models.IntegerField(db_column='Day6', blank=True, null=True)  # Field name made lowercase.
    day7 = models.IntegerField(db_column='Day7', blank=True, null=True)  # Field name made lowercase.
    day8 = models.IntegerField(db_column='Day8', blank=True, null=True)  # Field name made lowercase.
    day9 = models.IntegerField(db_column='Day9', blank=True, null=True)  # Field name made lowercase.
    day10 = models.IntegerField(db_column='Day10', blank=True, null=True)  # Field name made lowercase.
    day11 = models.IntegerField(db_column='Day11', blank=True, null=True)  # Field name made lowercase.
    day12 = models.IntegerField(db_column='Day12', blank=True, null=True)  # Field name made lowercase.
    day13 = models.IntegerField(db_column='Day13', blank=True, null=True)  # Field name made lowercase.
    day14 = models.IntegerField(db_column='Day14', blank=True, null=True)  # Field name made lowercase.
    day15 = models.IntegerField(db_column='Day15', blank=True, null=True)  # Field name made lowercase.
    day16 = models.IntegerField(db_column='Day16', blank=True, null=True)  # Field name made lowercase.
    day17 = models.IntegerField(db_column='Day17', blank=True, null=True)  # Field name made lowercase.
    day18 = models.IntegerField(db_column='Day18', blank=True, null=True)  # Field name made lowercase.
    day19 = models.IntegerField(db_column='Day19', blank=True, null=True)  # Field name made lowercase.
    day20 = models.IntegerField(db_column='Day20', blank=True, null=True)  # Field name made lowercase.
    day21 = models.IntegerField(db_column='Day21', blank=True, null=True)  # Field name made lowercase.
    day22 = models.IntegerField(db_column='Day22', blank=True, null=True)  # Field name made lowercase.
    day23 = models.IntegerField(db_column='Day23', blank=True, null=True)  # Field name made lowercase.
    day24 = models.IntegerField(db_column='Day24', blank=True, null=True)  # Field name made lowercase.
    day25 = models.IntegerField(db_column='Day25', blank=True, null=True)  # Field name made lowercase.
    day26 = models.IntegerField(db_column='Day26', blank=True, null=True)  # Field name made lowercase.
    day27 = models.IntegerField(db_column='Day27', blank=True, null=True)  # Field name made lowercase.
    day28 = models.IntegerField(db_column='Day28', blank=True, null=True)  # Field name made lowercase.
    day29 = models.IntegerField(db_column='Day29', blank=True, null=True)  # Field name made lowercase.
    day30 = models.IntegerField(db_column='Day30', blank=True, null=True)  # Field name made lowercase.
    day31 = models.IntegerField(db_column='Day31', blank=True, null=True)  # Field name made lowercase.
    januarymonthdata = models.IntegerField(db_column='JanuaryMonthData', blank=True, null=True)  # Field name made lowercase.
    panduan = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'carData_January'


class CardataJuly(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    day1 = models.IntegerField(db_column='Day1', blank=True, null=True)  # Field name made lowercase.
    day2 = models.IntegerField(db_column='Day2', blank=True, null=True)  # Field name made lowercase.
    day3 = models.IntegerField(db_column='Day3', blank=True, null=True)  # Field name made lowercase.
    day4 = models.IntegerField(db_column='Day4', blank=True, null=True)  # Field name made lowercase.
    day5 = models.IntegerField(db_column='Day5', blank=True, null=True)  # Field name made lowercase.
    day6 = models.IntegerField(db_column='Day6', blank=True, null=True)  # Field name made lowercase.
    day7 = models.IntegerField(db_column='Day7', blank=True, null=True)  # Field name made lowercase.
    day8 = models.IntegerField(db_column='Day8', blank=True, null=True)  # Field name made lowercase.
    day9 = models.IntegerField(db_column='Day9', blank=True, null=True)  # Field name made lowercase.
    day10 = models.IntegerField(db_column='Day10', blank=True, null=True)  # Field name made lowercase.
    day11 = models.IntegerField(db_column='Day11', blank=True, null=True)  # Field name made lowercase.
    day12 = models.IntegerField(db_column='Day12', blank=True, null=True)  # Field name made lowercase.
    day13 = models.IntegerField(db_column='Day13', blank=True, null=True)  # Field name made lowercase.
    day14 = models.IntegerField(db_column='Day14', blank=True, null=True)  # Field name made lowercase.
    day15 = models.IntegerField(db_column='Day15', blank=True, null=True)  # Field name made lowercase.
    day16 = models.IntegerField(db_column='Day16', blank=True, null=True)  # Field name made lowercase.
    day17 = models.IntegerField(db_column='Day17', blank=True, null=True)  # Field name made lowercase.
    day18 = models.IntegerField(db_column='Day18', blank=True, null=True)  # Field name made lowercase.
    day19 = models.IntegerField(db_column='Day19', blank=True, null=True)  # Field name made lowercase.
    day20 = models.IntegerField(db_column='Day20', blank=True, null=True)  # Field name made lowercase.
    day21 = models.IntegerField(db_column='Day21', blank=True, null=True)  # Field name made lowercase.
    day22 = models.IntegerField(db_column='Day22', blank=True, null=True)  # Field name made lowercase.
    day23 = models.IntegerField(db_column='Day23', blank=True, null=True)  # Field name made lowercase.
    day24 = models.IntegerField(db_column='Day24', blank=True, null=True)  # Field name made lowercase.
    day25 = models.IntegerField(db_column='Day25', blank=True, null=True)  # Field name made lowercase.
    day26 = models.IntegerField(db_column='Day26', blank=True, null=True)  # Field name made lowercase.
    day27 = models.IntegerField(db_column='Day27', blank=True, null=True)  # Field name made lowercase.
    day28 = models.IntegerField(db_column='Day28', blank=True, null=True)  # Field name made lowercase.
    day29 = models.IntegerField(db_column='Day29', blank=True, null=True)  # Field name made lowercase.
    day30 = models.IntegerField(db_column='Day30', blank=True, null=True)  # Field name made lowercase.
    day31 = models.IntegerField(db_column='Day31', blank=True, null=True)  # Field name made lowercase.
    julymonthdata = models.IntegerField(db_column='JulyMonthData', blank=True, null=True)  # Field name made lowercase.
    panduan = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'carData_July'


class CardataJune(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    day1 = models.IntegerField(db_column='Day1', blank=True, null=True)  # Field name made lowercase.
    day2 = models.IntegerField(db_column='Day2', blank=True, null=True)  # Field name made lowercase.
    day3 = models.IntegerField(db_column='Day3', blank=True, null=True)  # Field name made lowercase.
    day4 = models.IntegerField(db_column='Day4', blank=True, null=True)  # Field name made lowercase.
    day5 = models.IntegerField(db_column='Day5', blank=True, null=True)  # Field name made lowercase.
    day6 = models.IntegerField(db_column='Day6', blank=True, null=True)  # Field name made lowercase.
    day7 = models.IntegerField(db_column='Day7', blank=True, null=True)  # Field name made lowercase.
    day8 = models.IntegerField(db_column='Day8', blank=True, null=True)  # Field name made lowercase.
    day9 = models.IntegerField(db_column='Day9', blank=True, null=True)  # Field name made lowercase.
    day10 = models.IntegerField(db_column='Day10', blank=True, null=True)  # Field name made lowercase.
    day11 = models.IntegerField(db_column='Day11', blank=True, null=True)  # Field name made lowercase.
    day12 = models.IntegerField(db_column='Day12', blank=True, null=True)  # Field name made lowercase.
    day13 = models.IntegerField(db_column='Day13', blank=True, null=True)  # Field name made lowercase.
    day14 = models.IntegerField(db_column='Day14', blank=True, null=True)  # Field name made lowercase.
    day15 = models.IntegerField(db_column='Day15', blank=True, null=True)  # Field name made lowercase.
    day16 = models.IntegerField(db_column='Day16', blank=True, null=True)  # Field name made lowercase.
    day17 = models.IntegerField(db_column='Day17', blank=True, null=True)  # Field name made lowercase.
    day18 = models.IntegerField(db_column='Day18', blank=True, null=True)  # Field name made lowercase.
    day19 = models.IntegerField(db_column='Day19', blank=True, null=True)  # Field name made lowercase.
    day20 = models.IntegerField(db_column='Day20', blank=True, null=True)  # Field name made lowercase.
    day21 = models.IntegerField(db_column='Day21', blank=True, null=True)  # Field name made lowercase.
    day22 = models.IntegerField(db_column='Day22', blank=True, null=True)  # Field name made lowercase.
    day23 = models.IntegerField(db_column='Day23', blank=True, null=True)  # Field name made lowercase.
    day24 = models.IntegerField(db_column='Day24', blank=True, null=True)  # Field name made lowercase.
    day25 = models.IntegerField(db_column='Day25', blank=True, null=True)  # Field name made lowercase.
    day26 = models.IntegerField(db_column='Day26', blank=True, null=True)  # Field name made lowercase.
    day27 = models.IntegerField(db_column='Day27', blank=True, null=True)  # Field name made lowercase.
    day28 = models.IntegerField(db_column='Day28', blank=True, null=True)  # Field name made lowercase.
    day29 = models.IntegerField(db_column='Day29', blank=True, null=True)  # Field name made lowercase.
    day30 = models.IntegerField(db_column='Day30', blank=True, null=True)  # Field name made lowercase.
    day31 = models.IntegerField(db_column='Day31', blank=True, null=True)  # Field name made lowercase.
    junemonthdata = models.IntegerField(db_column='JuneMonthData', blank=True, null=True)  # Field name made lowercase.
    panduan = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'carData_June'


class CardataMarch(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    day1 = models.IntegerField(db_column='Day1', blank=True, null=True)  # Field name made lowercase.
    day2 = models.IntegerField(db_column='Day2', blank=True, null=True)  # Field name made lowercase.
    day3 = models.IntegerField(db_column='Day3', blank=True, null=True)  # Field name made lowercase.
    day4 = models.IntegerField(db_column='Day4', blank=True, null=True)  # Field name made lowercase.
    day5 = models.IntegerField(db_column='Day5', blank=True, null=True)  # Field name made lowercase.
    day6 = models.IntegerField(db_column='Day6', blank=True, null=True)  # Field name made lowercase.
    day7 = models.IntegerField(db_column='Day7', blank=True, null=True)  # Field name made lowercase.
    day8 = models.IntegerField(db_column='Day8', blank=True, null=True)  # Field name made lowercase.
    day9 = models.IntegerField(db_column='Day9', blank=True, null=True)  # Field name made lowercase.
    day10 = models.IntegerField(db_column='Day10', blank=True, null=True)  # Field name made lowercase.
    day11 = models.IntegerField(db_column='Day11', blank=True, null=True)  # Field name made lowercase.
    day12 = models.IntegerField(db_column='Day12', blank=True, null=True)  # Field name made lowercase.
    day13 = models.IntegerField(db_column='Day13', blank=True, null=True)  # Field name made lowercase.
    day14 = models.IntegerField(db_column='Day14', blank=True, null=True)  # Field name made lowercase.
    day15 = models.IntegerField(db_column='Day15', blank=True, null=True)  # Field name made lowercase.
    day16 = models.IntegerField(db_column='Day16', blank=True, null=True)  # Field name made lowercase.
    day17 = models.IntegerField(db_column='Day17', blank=True, null=True)  # Field name made lowercase.
    day18 = models.IntegerField(db_column='Day18', blank=True, null=True)  # Field name made lowercase.
    day19 = models.IntegerField(db_column='Day19', blank=True, null=True)  # Field name made lowercase.
    day20 = models.IntegerField(db_column='Day20', blank=True, null=True)  # Field name made lowercase.
    day21 = models.IntegerField(db_column='Day21', blank=True, null=True)  # Field name made lowercase.
    day22 = models.IntegerField(db_column='Day22', blank=True, null=True)  # Field name made lowercase.
    day23 = models.IntegerField(db_column='Day23', blank=True, null=True)  # Field name made lowercase.
    day24 = models.IntegerField(db_column='Day24', blank=True, null=True)  # Field name made lowercase.
    day25 = models.IntegerField(db_column='Day25', blank=True, null=True)  # Field name made lowercase.
    day26 = models.IntegerField(db_column='Day26', blank=True, null=True)  # Field name made lowercase.
    day27 = models.IntegerField(db_column='Day27', blank=True, null=True)  # Field name made lowercase.
    day28 = models.IntegerField(db_column='Day28', blank=True, null=True)  # Field name made lowercase.
    day29 = models.IntegerField(db_column='Day29', blank=True, null=True)  # Field name made lowercase.
    day30 = models.IntegerField(db_column='Day30', blank=True, null=True)  # Field name made lowercase.
    day31 = models.IntegerField(db_column='Day31', blank=True, null=True)  # Field name made lowercase.
    marchmonthdata = models.IntegerField(db_column='MarchMonthData', blank=True, null=True)  # Field name made lowercase.
    panduan = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'carData_March'


class CardataMay(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    day1 = models.IntegerField(db_column='Day1', blank=True, null=True)  # Field name made lowercase.
    day2 = models.IntegerField(db_column='Day2', blank=True, null=True)  # Field name made lowercase.
    day3 = models.IntegerField(db_column='Day3', blank=True, null=True)  # Field name made lowercase.
    day4 = models.IntegerField(db_column='Day4', blank=True, null=True)  # Field name made lowercase.
    day5 = models.IntegerField(db_column='Day5', blank=True, null=True)  # Field name made lowercase.
    day6 = models.IntegerField(db_column='Day6', blank=True, null=True)  # Field name made lowercase.
    day7 = models.IntegerField(db_column='Day7', blank=True, null=True)  # Field name made lowercase.
    day8 = models.IntegerField(db_column='Day8', blank=True, null=True)  # Field name made lowercase.
    day9 = models.IntegerField(db_column='Day9', blank=True, null=True)  # Field name made lowercase.
    day10 = models.IntegerField(db_column='Day10', blank=True, null=True)  # Field name made lowercase.
    day11 = models.IntegerField(db_column='Day11', blank=True, null=True)  # Field name made lowercase.
    day12 = models.IntegerField(db_column='Day12', blank=True, null=True)  # Field name made lowercase.
    day13 = models.IntegerField(db_column='Day13', blank=True, null=True)  # Field name made lowercase.
    day14 = models.IntegerField(db_column='Day14', blank=True, null=True)  # Field name made lowercase.
    day15 = models.IntegerField(db_column='Day15', blank=True, null=True)  # Field name made lowercase.
    day16 = models.IntegerField(db_column='Day16', blank=True, null=True)  # Field name made lowercase.
    day17 = models.IntegerField(db_column='Day17', blank=True, null=True)  # Field name made lowercase.
    day18 = models.IntegerField(db_column='Day18', blank=True, null=True)  # Field name made lowercase.
    day19 = models.IntegerField(db_column='Day19', blank=True, null=True)  # Field name made lowercase.
    day20 = models.IntegerField(db_column='Day20', blank=True, null=True)  # Field name made lowercase.
    day21 = models.IntegerField(db_column='Day21', blank=True, null=True)  # Field name made lowercase.
    day22 = models.IntegerField(db_column='Day22', blank=True, null=True)  # Field name made lowercase.
    day23 = models.IntegerField(db_column='Day23', blank=True, null=True)  # Field name made lowercase.
    day24 = models.IntegerField(db_column='Day24', blank=True, null=True)  # Field name made lowercase.
    day25 = models.IntegerField(db_column='Day25', blank=True, null=True)  # Field name made lowercase.
    day26 = models.IntegerField(db_column='Day26', blank=True, null=True)  # Field name made lowercase.
    day27 = models.IntegerField(db_column='Day27', blank=True, null=True)  # Field name made lowercase.
    day28 = models.IntegerField(db_column='Day28', blank=True, null=True)  # Field name made lowercase.
    day29 = models.IntegerField(db_column='Day29', blank=True, null=True)  # Field name made lowercase.
    day30 = models.IntegerField(db_column='Day30', blank=True, null=True)  # Field name made lowercase.
    day31 = models.IntegerField(db_column='Day31', blank=True, null=True)  # Field name made lowercase.
    maymonthdata = models.IntegerField(db_column='MayMonthData', blank=True, null=True)  # Field name made lowercase.
    panduan = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'carData_May'


class CardataNovember(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    day1 = models.IntegerField(db_column='Day1', blank=True, null=True)  # Field name made lowercase.
    day2 = models.IntegerField(db_column='Day2', blank=True, null=True)  # Field name made lowercase.
    day3 = models.IntegerField(db_column='Day3', blank=True, null=True)  # Field name made lowercase.
    day4 = models.IntegerField(db_column='Day4', blank=True, null=True)  # Field name made lowercase.
    day5 = models.IntegerField(db_column='Day5', blank=True, null=True)  # Field name made lowercase.
    day6 = models.IntegerField(db_column='Day6', blank=True, null=True)  # Field name made lowercase.
    day7 = models.IntegerField(db_column='Day7', blank=True, null=True)  # Field name made lowercase.
    day8 = models.IntegerField(db_column='Day8', blank=True, null=True)  # Field name made lowercase.
    day9 = models.IntegerField(db_column='Day9', blank=True, null=True)  # Field name made lowercase.
    day10 = models.IntegerField(db_column='Day10', blank=True, null=True)  # Field name made lowercase.
    day11 = models.IntegerField(db_column='Day11', blank=True, null=True)  # Field name made lowercase.
    day12 = models.IntegerField(db_column='Day12', blank=True, null=True)  # Field name made lowercase.
    day13 = models.IntegerField(db_column='Day13', blank=True, null=True)  # Field name made lowercase.
    day14 = models.IntegerField(db_column='Day14', blank=True, null=True)  # Field name made lowercase.
    day15 = models.IntegerField(db_column='Day15', blank=True, null=True)  # Field name made lowercase.
    day16 = models.IntegerField(db_column='Day16', blank=True, null=True)  # Field name made lowercase.
    day17 = models.IntegerField(db_column='Day17', blank=True, null=True)  # Field name made lowercase.
    day18 = models.IntegerField(db_column='Day18', blank=True, null=True)  # Field name made lowercase.
    day19 = models.IntegerField(db_column='Day19', blank=True, null=True)  # Field name made lowercase.
    day20 = models.IntegerField(db_column='Day20', blank=True, null=True)  # Field name made lowercase.
    day21 = models.IntegerField(db_column='Day21', blank=True, null=True)  # Field name made lowercase.
    day22 = models.IntegerField(db_column='Day22', blank=True, null=True)  # Field name made lowercase.
    day23 = models.IntegerField(db_column='Day23', blank=True, null=True)  # Field name made lowercase.
    day24 = models.IntegerField(db_column='Day24', blank=True, null=True)  # Field name made lowercase.
    day25 = models.IntegerField(db_column='Day25', blank=True, null=True)  # Field name made lowercase.
    day26 = models.IntegerField(db_column='Day26', blank=True, null=True)  # Field name made lowercase.
    day27 = models.IntegerField(db_column='Day27', blank=True, null=True)  # Field name made lowercase.
    day28 = models.IntegerField(db_column='Day28', blank=True, null=True)  # Field name made lowercase.
    day29 = models.IntegerField(db_column='Day29', blank=True, null=True)  # Field name made lowercase.
    day30 = models.IntegerField(db_column='Day30', blank=True, null=True)  # Field name made lowercase.
    day31 = models.IntegerField(db_column='Day31', blank=True, null=True)  # Field name made lowercase.
    novembermonthdata = models.IntegerField(db_column='NovemberMonthData', blank=True, null=True)  # Field name made lowercase.
    panduan = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'carData_November'


class CardataOctober(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    day1 = models.IntegerField(db_column='Day1', blank=True, null=True)  # Field name made lowercase.
    day2 = models.IntegerField(db_column='Day2', blank=True, null=True)  # Field name made lowercase.
    day3 = models.IntegerField(db_column='Day3', blank=True, null=True)  # Field name made lowercase.
    day4 = models.IntegerField(db_column='Day4', blank=True, null=True)  # Field name made lowercase.
    day5 = models.IntegerField(db_column='Day5', blank=True, null=True)  # Field name made lowercase.
    day6 = models.IntegerField(db_column='Day6', blank=True, null=True)  # Field name made lowercase.
    day7 = models.IntegerField(db_column='Day7', blank=True, null=True)  # Field name made lowercase.
    day8 = models.IntegerField(db_column='Day8', blank=True, null=True)  # Field name made lowercase.
    day9 = models.IntegerField(db_column='Day9', blank=True, null=True)  # Field name made lowercase.
    day10 = models.IntegerField(db_column='Day10', blank=True, null=True)  # Field name made lowercase.
    day11 = models.IntegerField(db_column='Day11', blank=True, null=True)  # Field name made lowercase.
    day12 = models.IntegerField(db_column='Day12', blank=True, null=True)  # Field name made lowercase.
    day13 = models.IntegerField(db_column='Day13', blank=True, null=True)  # Field name made lowercase.
    day14 = models.IntegerField(db_column='Day14', blank=True, null=True)  # Field name made lowercase.
    day15 = models.IntegerField(db_column='Day15', blank=True, null=True)  # Field name made lowercase.
    day16 = models.IntegerField(db_column='Day16', blank=True, null=True)  # Field name made lowercase.
    day17 = models.IntegerField(db_column='Day17', blank=True, null=True)  # Field name made lowercase.
    day18 = models.IntegerField(db_column='Day18', blank=True, null=True)  # Field name made lowercase.
    day19 = models.IntegerField(db_column='Day19', blank=True, null=True)  # Field name made lowercase.
    day20 = models.IntegerField(db_column='Day20', blank=True, null=True)  # Field name made lowercase.
    day21 = models.IntegerField(db_column='Day21', blank=True, null=True)  # Field name made lowercase.
    day22 = models.IntegerField(db_column='Day22', blank=True, null=True)  # Field name made lowercase.
    day23 = models.IntegerField(db_column='Day23', blank=True, null=True)  # Field name made lowercase.
    day24 = models.IntegerField(db_column='Day24', blank=True, null=True)  # Field name made lowercase.
    day25 = models.IntegerField(db_column='Day25', blank=True, null=True)  # Field name made lowercase.
    day26 = models.IntegerField(db_column='Day26', blank=True, null=True)  # Field name made lowercase.
    day27 = models.IntegerField(db_column='Day27', blank=True, null=True)  # Field name made lowercase.
    day28 = models.IntegerField(db_column='Day28', blank=True, null=True)  # Field name made lowercase.
    day29 = models.IntegerField(db_column='Day29', blank=True, null=True)  # Field name made lowercase.
    day30 = models.IntegerField(db_column='Day30', blank=True, null=True)  # Field name made lowercase.
    day31 = models.IntegerField(db_column='Day31', blank=True, null=True)  # Field name made lowercase.
    octobermonthdata = models.IntegerField(db_column='OctoberMonthData', blank=True, null=True)  # Field name made lowercase.
    panduan = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'carData_October'


class CardataSeptember(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    day1 = models.IntegerField(db_column='Day1', blank=True, null=True)  # Field name made lowercase.
    day2 = models.IntegerField(db_column='Day2', blank=True, null=True)  # Field name made lowercase.
    day3 = models.IntegerField(db_column='Day3', blank=True, null=True)  # Field name made lowercase.
    day4 = models.IntegerField(db_column='Day4', blank=True, null=True)  # Field name made lowercase.
    day5 = models.IntegerField(db_column='Day5', blank=True, null=True)  # Field name made lowercase.
    day6 = models.IntegerField(db_column='Day6', blank=True, null=True)  # Field name made lowercase.
    day7 = models.IntegerField(db_column='Day7', blank=True, null=True)  # Field name made lowercase.
    day8 = models.IntegerField(db_column='Day8', blank=True, null=True)  # Field name made lowercase.
    day9 = models.IntegerField(db_column='Day9', blank=True, null=True)  # Field name made lowercase.
    day10 = models.IntegerField(db_column='Day10', blank=True, null=True)  # Field name made lowercase.
    day11 = models.IntegerField(db_column='Day11', blank=True, null=True)  # Field name made lowercase.
    day12 = models.IntegerField(db_column='Day12', blank=True, null=True)  # Field name made lowercase.
    day13 = models.IntegerField(db_column='Day13', blank=True, null=True)  # Field name made lowercase.
    day14 = models.IntegerField(db_column='Day14', blank=True, null=True)  # Field name made lowercase.
    day15 = models.IntegerField(db_column='Day15', blank=True, null=True)  # Field name made lowercase.
    day16 = models.IntegerField(db_column='Day16', blank=True, null=True)  # Field name made lowercase.
    day17 = models.IntegerField(db_column='Day17', blank=True, null=True)  # Field name made lowercase.
    day18 = models.IntegerField(db_column='Day18', blank=True, null=True)  # Field name made lowercase.
    day19 = models.IntegerField(db_column='Day19', blank=True, null=True)  # Field name made lowercase.
    day20 = models.IntegerField(db_column='Day20', blank=True, null=True)  # Field name made lowercase.
    day21 = models.IntegerField(db_column='Day21', blank=True, null=True)  # Field name made lowercase.
    day22 = models.IntegerField(db_column='Day22', blank=True, null=True)  # Field name made lowercase.
    day23 = models.IntegerField(db_column='Day23', blank=True, null=True)  # Field name made lowercase.
    day24 = models.IntegerField(db_column='Day24', blank=True, null=True)  # Field name made lowercase.
    day25 = models.IntegerField(db_column='Day25', blank=True, null=True)  # Field name made lowercase.
    day26 = models.IntegerField(db_column='Day26', blank=True, null=True)  # Field name made lowercase.
    day27 = models.IntegerField(db_column='Day27', blank=True, null=True)  # Field name made lowercase.
    day28 = models.IntegerField(db_column='Day28', blank=True, null=True)  # Field name made lowercase.
    day29 = models.IntegerField(db_column='Day29', blank=True, null=True)  # Field name made lowercase.
    day30 = models.IntegerField(db_column='Day30', blank=True, null=True)  # Field name made lowercase.
    day31 = models.IntegerField(db_column='Day31', blank=True, null=True)  # Field name made lowercase.
    septembermonthdata = models.IntegerField(db_column='SeptemberMonthData', blank=True, null=True)  # Field name made lowercase.
    panduan = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'carData_September'


class CardataYear(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    entercardata = models.IntegerField(db_column='EnterCarData', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'carData_Year'
