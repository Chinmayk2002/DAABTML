// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    struct Student {
        uint256 id;
        string name;
        uint256 age;
        uint256 marks;
    }

    Student[] public students;

    event StudentAdded(uint256 id, string name, uint256 age, uint256 marks);

    fallback() external {
        revert("Fallback function is not allowed.");
    }

    function addStudent(uint256 _id, string memory _name, uint256 _age, uint256 _marks) public {
        students.push(Student(_id, _name, _age, _marks));
        emit StudentAdded(_id, _name, _age, _marks);
    }

    function getStudentCount() public view returns (uint256) {
        return students.length;
    }

    function getStudent(uint256 index) public view returns (uint256, string memory, uint256, uint256) {
        require(index < students.length, "Invalid index");
        return (students[index].id, students[index].name, students[index].age, students[index].marks);
    }
}