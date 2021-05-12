
#include <string>
#include <algorithm>
#include <iostream>

template <typename T>
class DynamicArray
{
    T* data;
    size_t n;



public:
    DynamicArray(int n)
    {
        this->n = n;
        data = new T[n];
    }
    DynamicArray(const DynamicArray<T>& other)
    {
        n = other.n;
        data = new T[n];

        for(int i = 0; i < n; i++)
        {
            data[i] = other[n];
        }

    }
    T& operator[](int index)
    {
        return data[index];
    }

    const T& operator[](int index) const
    {
        return data[index];
    }

    T& at(int index)
    {
        if (index < n)
            return data[index];
        throw "Index out of range";
    }

    size_t size()
    {
        return n;
    }
    ~DynamicArray()
    {
        delete[] data;
    }

    T* begin() {return data;}

    const T* begin() const {return data;}

    T* end() {return data + n;}

    const T* end() const {return data + n;}

    friend DynamicArray<T> operator+(const DynamicArray<T>& arr1, DynamicArray<T>& arr2)
    {
        DynamicArray<T> result(arr1.size() + arr2.size());
        std::copy(arr1.begin(), arr1.end, result.begin());
        std::copy(arr2.begin(), arr2.end, result.begin() + arr1.size());
        
        return result;
    }

    std::string to_string(const std::string& sep = ", ")
    {
        if(n == 0)
            return "";
        
        std::ostringstream os;
        os << data[0];
        for(int i = 1; i < n; i++)
            os << sep << data[i];
        
        return os.str();
    }

    struct student
    {
        std::string name;
        int standard;
    };
    
    std::ostream& operator<<(std::ostream& os, const student& s)
    {
        return (os << "[" << s.name << ", " << s.standard << "]");
    }

    int main()
    {
        int nStudents;
        std::cout << "1반 학생 수를 입력하세요: ";
        std:cin >> nStudents;

        
    }
};

