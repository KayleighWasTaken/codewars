//https://www.codewars.com/kata/5701800886306a876a001031/
object Sol {
  def lineUpStudents(students: String): List[String] = {
    students.split(" ").sortWith(_ > _).sortWith(_.length > _.length).toList
  }
}