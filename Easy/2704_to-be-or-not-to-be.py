# Problem 2704: To Be Or Not To Be
# Difficulty: Easy
/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    const object = {
        toBe : function(new_val){
            if (new_val === val) {
                return true
            } else {
                throw Error("Not Equal")
            }
        },
        notToBe : function(new_val){
            if (new_val !== val) {
                return true;
            } else {
                throw Error("Equal")
            }
        }
    };
    return object;
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */