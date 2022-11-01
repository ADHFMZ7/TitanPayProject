cPrev = -1; 

function sortBy(col) {
    rows = document.getElementById("sortable").rows.length;
    columns = document.getElementById("sortable").rows[0].cells.length; 
    arrTable = [...Array(rows)].map(e => Array(columns)); 

    for (i=0; i<rows; i++) { 
        for (j=0; j<columns; j++) { 
            
            arrTable[i][j] = document.getElementById("sortable").rows[i].cells[j].innerHTML;
        }
    }

    th = arrTable.shift(); 
    
    if (col !== cPrev) { 
        arrTable.sort(
            function (a, b) {
                if (a[col] === b[col]) {
                    return 0;
                } else {
                    if (a[col] < b[col]){
                        return -1
                    } else {
                        return 1
                    }
                }
            }
        );
    } else { 
        arrTable.reverse();
    }
    
    cPrev = col; 

    arrTable.unshift(th);

    for (i=0; i<rows; i++) {
        for (j=0; j<columns; j++) {
            document.getElementById("sortable").rows[i].cells[j].innerHTML = arrTable[i][j];
        }
    }
}