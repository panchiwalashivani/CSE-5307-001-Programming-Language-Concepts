/**
 * Name: Shivani Panchiwala
 * Student ID: 1001982478
 * Date: 7th March 2023
 * Used below command to run the file
 * node lab02smp2478.js 
 */

console.log('Que1')
const num1 = 10
const inputtable = [...Array(num1).keys()].map(x => x+1)
console.log(inputtable)
// Using spread operator and Array().keys() created array of 10
// To increment each element by 1 by map function


console.log('Que2')
// To multiply each element in inputable by 5 using map function
const fiveTable = inputtable.map(x => x*5)
console.log(fiveTable)

// To multiply each element in inputable by 13 using map function
const thirteenTable = inputtable.map(x => x*13)
console.log(thirteenTable)

// To multiply each element in inputable by the elemtn itself using map function
const squaresTable = inputtable.map(x => x*x)
console.log(squaresTable)



console.log('Que3')
const num100 = 100
// Using spread operator and Array().keys() created array of 100
// To increment each element by 1 using map function
// To keep only the mulltiples of 5 by using filter function
const multiple_Five = [...Array(num100).keys()].map(x => x+1).filter(x => x%5 === 0)


// To check if remainder is 1 for odd 
const odd_Five_Multiple = multiple_Five.filter(x => x%2 === 1)
console.log(odd_Five_Multiple)



console.log('Que4')
// Using spread operator and Array().keys() created array of 100
// To increment each element by 1 using map function
// To keep only the mulltiples of 7 by using filter function
const multiple_Seven = [...Array(num100).keys()].map(x => x+1).filter(x => x%7 === 0)


// To check if remainder is 0 for even
const even_multiple_Seven = multiple_Seven.filter(x => x%2 === 0)
console.log(even_multiple_Seven)

// using reduce to add all elements in even_multiple_Seven array
const sum_even_multiple_Seven = even_multiple_Seven.reduce((acc, x) => acc+x)
console.log(`\nSum of even multiples of 7 between 1 and 100 = ${sum_even_multiple_Seven}`)



console.log('Que5')

// defined a currying function
const cylinder_volume = r => h => 3.14*r*r*h

// As first argument only passing r = 5 in the currying function 
const cylinder_Radius_5 = cylinder_volume(5)

// As the second argument passing value of h in the currying function
const volume_Height_10 = cylinder_Radius_5(10)
console.log(`volume_Height_10 = ${volume_Height_10}`)

// As the second argument passing value of h in the currying function
const volume_Height_17 = cylinder_Radius_5(17)
console.log(`volume_Height_17 = ${volume_Height_17}`)

// As the second argument passing value of h in the currying function
const volume_Height_11 = cylinder_Radius_5(11)
console.log(`volume_Height_11 = ${volume_Height_11}`)



console.log('Que6')

// From lab pdf
const Tag = (begin_Tag, end_Tag) => {
    return (text_Content) => '\n' + begin_Tag + text_Content + end_Tag
}

// creating all the required tags
const table_Tag = Tag('<table>', '</table>')
const tr_Tag = Tag('<tr>','</tr>')
const th_Tag = Tag('<th>','</th>')
const row_Heading = tr_Tag(th_Tag('First Name') + th_Tag('Last Name') + th_Tag('Age') + '\n')
const row_Data1 = tr_Tag(th_Tag('Shripal') + th_Tag('Panchiwala') + th_Tag('20') + '\n')
const row_Data2 = tr_Tag(th_Tag('Shivani') + th_Tag('Modi') + th_Tag('23') + '\n')
const row_Data3 = tr_Tag(th_Tag('Sundeep') + th_Tag('Kukkala') + th_Tag('25') + '\n')

// All the created tags are combined in the correct order
const output = table_Tag(row_Heading+'\n'+row_Data1+'\n'+row_Data2+'\n'+row_Data3+'\n')
console.log(output)



console.log('Que7')
console.log('For even or odd, use arguments as \"even\" or \"odd\"')

// To generalize Q3 and Q4 used closures and currying
const generalize = multipleOf => {
    const num100 = 100
    // Using spread operator and Array().keys() created array of size 100
    // To increment each element by 1 using map function
    const arr100 = [...Array(num100).keys()].map(x => x+1)

    // To keep only the mulltiples using filter function
    const multiple = arr100.filter(x => x%multipleOf === 0)
    
    // expects string "even" or "odd"
    return (type) => {
        // used to filter even numbers
        if (type === 'even'){
            // To keep only even numbers using filter function
            return multiple.filter(x => x%2 === 0)
        }
        // used to filter odd numbers
        else if (type === 'odd'){
            // To keep only odd numbers using filter function
            return multiple.filter(x => x%2 === 1)
        }
        // handles unexpected string inputs
        else {
            throw Error('The expected types are even and odd. Unexpected input.')
        }
    }
}

// passing first argument to currying function
const multiple_5 = generalize(5)
// passing second argument to currying function
const odd_Multiple_5 = multiple_5('odd')
console.log('Q3 general version\n')
console.log(odd_Multiple_5)

// passing first argument to currying function
const multiple_7 = generalize(7)
// passing second argument to currying function
const even_Multiple_7 = multiple_7('even')
console.log('Q4 general version\n')
console.log(even_Multiple_7)