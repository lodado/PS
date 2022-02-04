/**
 * @param {number} k
 */
var MyCircularQueue = function(k) {
    this.queue = Array.from({length : k}, ()=> null);
    this.front = 0;
    this.back = 0;
    this.size = k;
};

/** 
 * @param {number} value
 * @return {boolean}
 */
MyCircularQueue.prototype.enQueue = function(value) {
    
    if(this.queue[this.back] === null){
        this.queue[this.back] = value;
        this.back = (this.back+1) % this.size;
        return true;
    }
    
    return false;
};

/**
 * @return {boolean}
 */
MyCircularQueue.prototype.deQueue = function() {
    
    if(this.queue[this.front] !== null){
        this.queue[this.front] = null;
        this.front = (this.front+1) % this.size;
        return true;
    }
    
    return false;
    
};

/**
 * @return {number}
 */
MyCircularQueue.prototype.Front = function() {
    return this.queue[this.front] ?? -1;
};

/**
 * @return {number}
 */
MyCircularQueue.prototype.Rear = function() {
    const beforeBack = (this.back-1)>=0 ? this.back-1 : this.size-1;
    return this.queue[beforeBack] ?? -1;
};

/**
 * @return {boolean}
 */
MyCircularQueue.prototype.isEmpty = function() {
    return this.front === this.back && this.queue[this.front] === null;
};

/**
 * @return {boolean}
 */
MyCircularQueue.prototype.isFull = function() {
    return this.front === this.back && this.queue[this.front] !== null;
};

/** 
 * Your MyCircularQueue object will be instantiated and called as such:
 * var obj = new MyCircularQueue(k)
 * var param_1 = obj.enQueue(value)
 * var param_2 = obj.deQueue()
 * var param_3 = obj.Front()
 * var param_4 = obj.Rear()
 * var param_5 = obj.isEmpty()
 * var param_6 = obj.isFull()
 */
