import java.io._

object Main
{
  def main(args: Array[String]): Unit = {
    val start = System.nanoTime()
    for( i <- 0 to 10) {
    }
    val end = System.nanoTime()
    val elapsed = (end - start)  / 1_000_000

    println("Took: " + elapsed + " milliseconds")

    val fileWriter = new FileWriter("output.txt", true)

    fileWriter.write(elapsed.toString)
    fileWriter.write("\n")

    fileWriter.close()
  }
}
