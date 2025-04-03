function second_largest(arr){

    n=arr.length
    let first =Number.NEGATIVE_INFINITY
    let second =Number.NEGATIVE_INFINITY
    for (let i=0 ; i<n; i++){
        if (arr[i]>first){
            second=first;
            first=arr[i];
        }
        else if(arr[i]!==first && arr[i]>second){
            second=arr[i]
        }
    }
    if (second === Number.NEGATIVE_INFINITY) {
        return null ;
    }

    return second

}

let arr = [56, 89, 90, 45, 78, 95, 97];
console.log(second_largest(arr)); // Output: 95