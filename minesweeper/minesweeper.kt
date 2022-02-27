package minesweeper

import kotlin.random.Random

fun showGrid(playerGrid: BooleanArray, hintsGrid: IntArray) {
    println(" │123456789│")
    println("—│—————————│")
    var cell = 0
    for (i in 1..9) {
        print("$i|")
        repeat(9) {
            if (playerGrid[cell])
                print("*")
            else {
                if (hintsGrid[cell] == 0)
                    print(".")
                else
                    print(hintsGrid[cell])
            }
            cell++
        }
        println("|")
    }  
    println("—│—————————│")
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

fun generateHints(grid: BooleanArray, hintsGrid: IntArray) {
    var cell = 0
    val neigborhoodFull = intArrayOf(-10, -9, -8, -1, 1, 8, 9, 10)
    val neigborhoodLeft = intArrayOf(-10, -9, -1, 8, 9)
    val neigborhoodRight = intArrayOf(-9, -8, 1, 9, 10)
    var neigborhood = neigborhoodFull
    var index = 0
    var nbMines = 0
    repeat(9) {
        repeat(9) {
            if (! grid[cell]) {
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
                hintsGrid[cell] = nbMines
            }
            cell++
        }
    }
}  

fun main() {
    val grid = BooleanArray(9 * 9)
    val playerGrid = BooleanArray(9 * 9)
    val hintsGrid = IntArray(9 * 9)
    print("How many mines do you want on the field?")
    val nbMines = readLine()!!.toInt()
    generateMines(grid, nbMines)
    generateHints(grid, hintsGrid)
    var posX = 0
    var posY = 0
    var cellNumber = 0
    var validInput = false
    while (! (playerGrid contentEquals grid)) {
        showGrid(playerGrid, hintsGrid)
        validInput = false
        while (! validInput) {
            print("Set/delete mine marks (x and y coordinates):")
            var coord = readLine()!!.split(" ")
            posX = coord[0].toInt()
            posY = coord[1].toInt()
            cellNumber = (posY - 1) * 9 + (posX - 1)
            if (hintsGrid[cellNumber] > 0) 
                println("There is a number here!")
            else   
                validInput = true
        } 
        playerGrid[cellNumber] = !playerGrid[cellNumber]
    }
    showGrid(playerGrid, hintsGrid)
    println("Congratulations! You found all the mines!")
}