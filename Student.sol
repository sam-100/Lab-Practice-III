// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    struct Student {
        uint256 id;
        string name;
        uint256 age;
        string course;
    }

    Student[] public students;

    fallback() external payable {}

    receive() external payable {}

    function addStudent(uint256 _id, string memory _name, uint256 _age, string memory _course) external {
        Student memory newStudent = Student(_id, _name, _age, _course);
        students.push(newStudent);
    }

    function getStudentCount() external view returns (uint256) {
        return students.length;
    }

    function getStudent(uint256 index) external view returns (uint256, string memory, uint256, string memory) {
        require(index < students.length, "Index out of bounds");

        Student memory student = students[index];
        return (student.id, student.name, student.age, student.course);
    }
}
