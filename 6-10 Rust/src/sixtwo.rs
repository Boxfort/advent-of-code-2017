fn get_max_index(array: &[i32]) -> usize {
    let mut i = 0;
    let mut max = 0;

    for j in 0..array.len() {
        if array[j] > max {
            i = j;
            max = array[j];
        }
    }

    return i;
}

fn redistribute_bucket(array: &mut[i32], bucket: usize) {
    let to_redist = array[bucket];
    let array_len = array.len();
    array[bucket] = 0;
    for i in 1..to_redist + 1{
        array[(bucket+i as usize) % array_len] += 1;
    }
}

pub fn run() {
    let mut buckets: [i32; 16] = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5];
    let mut history: Vec<[i32; 16]> = Vec::new();

    let mut steps = 0;

    while !history.contains(&buckets) {
        history.push(buckets);
        let i = get_max_index(&buckets);
        redistribute_bucket(&mut buckets,i);
    }

    // Clear History, re-run
    history.clear();

    while !history.contains(&buckets) {
        history.push(buckets);
        let i = get_max_index(&buckets);
        redistribute_bucket(&mut buckets,i);
        steps += 1;
    }

    println!("{:?}", steps);
}
