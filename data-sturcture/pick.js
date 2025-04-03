function peak(arr){
    let n =arr.length
    if (n===1){
        return arr[0]
    }
    let num = [] ;
    if (arr[0]>arr[1]){
        num.push(arr[0])
    }

    for (let i=1; i<n-1;i++){
        if (arr[i]>arr[i-1] && arr[i]>arr[i+1]){
            num.push(arr[i])
        }
    }
    if (arr[n-1]>arr[n-2]){
        num.push(arr[n-1])
    }
    return num.length !== 0 ? num : -1


}




let arr = [10, 20, 15, 2, 23, 90, 80];
console.log(peak(arr));