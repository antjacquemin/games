package minesweeper

import kotlin.random.Random

fun showGrid(grid: BooleanArray) {
    var cell = 0
    repeat(9) {
        repeat(9) {
            if (grid[cell])
                print("X")
            else
                print(".")
            cell++
        }
        println()
    }  
}

fun generateMines(grid: BooleanArray, nbMines: Int) {
    var cell: Int
    repeat(nbMines) {
        do {
            cell = Random.nextInt(80)
        } while (grid[cell])
        grid[cell] = true
    }
}

fun main() {
    val grid = BooleanArray(9 * 9)
    print("How many mines do you want on the field?")
    val nbMines = readLine()!!.toInt()
    generateMines(grid, nbMines)
    showGrid(grid)
}