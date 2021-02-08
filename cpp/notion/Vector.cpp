class Vector{
    public:
        int capacity, size;
        int *vc;

        Vector() {
            capacity = 8;
            size = 0;
            vc = new int[capacity];
        }
        ~Vector(){
            delete[] vc;
        }
        void push_back(int val){
            if(capacity == size){
                capacity *= 2;
                int *temp = new int[capacity];
                for(int i = 0; i < size; i++){
                    temp[i] = vc[i];
                }
                delete vc;
                vc = temp;
            }
            vc[size++] = val;
        }
        int getSize(){
            return size;
        }
        bool isEmpty(){
            return !size;
        }
        void clear(){
            delete vc;
            vc = new int[capacity];
            size = 0;
        }
        int &operator[](int i){
            return vc[i];
        }

}