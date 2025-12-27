; ModuleID = "/home/printrush/PycharmProjects/bmstu_python/laboratory_work_09/v2.0/codegen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry:
  %".2" = add i32 5, 3
  %".3" = bitcast [4 x i8]* @"fstr_int_1" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 %".2")
  %".5" = mul i32 2, 2
  %".6" = bitcast [4 x i8]* @"fstr_int_2" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i32 %".5")
  %".8" = sdiv i32 10, 2
  %".9" = bitcast [4 x i8]* @"fstr_int_3" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %".8")
  %".11" = bitcast [4 x i8]* @"fstr_str_4" to i8*
  %".12" = bitcast [14 x i8]* @".str.3511" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".11", i8* %".12")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"fstr_int_1" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_int_2" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_int_3" = internal constant [4 x i8] c"%d\0a\00"
@".str.3511" = internal constant [14 x i8] c"Hello, World!\00"
@"fstr_str_4" = internal constant [4 x i8] c"%s\0a\00"