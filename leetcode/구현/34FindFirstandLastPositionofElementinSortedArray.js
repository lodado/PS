/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    let arr = [-1, -1];
    let index =0;
    
    for(let i in nums){
        
        if(arr[0]===-1 && nums[i]===target){
            arr[0]=i;
        }   
        
        if(arr[0]!==-1 && nums[i]===target){
            arr[1]=i;
        } 
    }
    
    return arr;
};
