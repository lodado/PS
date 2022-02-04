/**
 * @param {number} k
 */
const MyCircularQueue = function(k) {
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
