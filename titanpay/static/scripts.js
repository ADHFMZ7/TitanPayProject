

cPrev = -1; 

function sortBy(c) {
    rows = document.getElementById("sortable").rows.length;
    columns = document.getElementById("sortable").rows[0].cells.length; 
    arrTable = [...Array(rows)].map(e => Array(columns)); 

    for (ro=0; ro<rows; ro++) { 
        for (co=0; co<columns; co++) { 
            
            arrTable[ro][co] = document.getElementById("sortable").rows[ro].cells[co].innerHTML;
        }
    }

    th = arrTable.shift(); 
    
    if (c !== cPrev) { 
        arrTable.sort(
            function (a, b) {
                if (a[c] === b[c]) {
                    return 0;
                } else {
                    return (a[c] < b[c]) ? -1 : 1;
                }
            }
        );
    } else { 
        arrTable.reverse();
    }
    
    cPrev = c; 

    arrTable.unshift(th);

    for (ro=0; ro<rows; ro++) {
        for (co=0; co<columns; co++) {
            document.getElementById("sortable").rows[ro].cells[co].innerHTML = arrTable[ro][co];
        }
    }
}