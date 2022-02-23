package minesweeper

import kotlin.random.Random

fun showGrid(grid: BooleanArray) {
    var cell = 0
    val neigborhoodFull = intArrayOf(-10, -9, -8, -1, 1, 8, 9, 10)
    val neigborhoodLeft = intArrayOf(-10, -9, -1, 8, 9)
    val neigborhoodRight = intArrayOf(-9, -8, 1, 9, 10)
    var neigborhood = neigborhoodFull
    var index = 0
    var nbMines = 0
    repeat(9) {
        repeat(9) {
            if (grid[cell])
                print("X")
            else {
                nbMines = 0
                when {
                    cell % 9 == 0 -> neigborhood = neigborhoodRight
                    cell % 9 == 8 -> neigborhood = neigborhoodLeft
                    else -> neigborhood = neigborhoodFull 
                }
                for (i in neigborhood) {
                    index = cell + i
                    if (index > -1 && index < 81 && grid[index])
                        nbMines++
                }
                if (nbMines == 0)
                    print(".")
                else
                    print(nbMines)
            }
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