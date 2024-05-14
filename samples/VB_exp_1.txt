Imports System

Module DataOperationWithDatabase

    MustInherit Class DataOperation
        Public MustOverride Function PerformOperation(ByVal Input As Integer) As Integer
    End Class

    Class AdditionOperation
        Inherits DataOperation
        Public Overrides Function PerformOperation(ByVal Input As Integer) As Integer
            Return Input + 10
        End Function
    End Class

    Class SubtractionOperation
        Inherits DataOperation
        Public Overrides Function PerformOperation(ByVal Input As Integer) As Integer
            Return Input - 5
        End Function
    End Class

    Module DatabaseUpdater
        Public Sub UpdateDatabase(ByVal OperationName As String, ByVal Input As Integer, ByVal Output As Integer)
            Console.WriteLine("Updating database with operation: " & OperationName & ", Input: " & Input & ", Output: " & Output)
            ' Code to update the database with the operation details
        End Sub
    End Module

    Sub Main()
        Try
            Console.WriteLine("Welcome to Data Operation Program")

            ' Input operation type
            Console.Write("Enter operation type (A for Addition, S for Subtraction): ")
            Dim OperationType As Char = Console.ReadLine().ToUpper()

            ' Input number
            Console.Write("Enter a number: ")
            Dim InputNumber As Integer = Integer.Parse(Console.ReadLine())

            Dim Operation As DataOperation = Nothing

            ' Perform operation based on user input
            Select Case OperationType
                Case "A"
                    Operation = New AdditionOperation()
                Case "S"
                    Operation = New SubtractionOperation()
                Case Else
                    Console.WriteLine("Invalid operation type.")
                    Exit Sub
            End Select

            Dim OutputNumber As Integer = Operation.PerformOperation(InputNumber)

            ' Output result to the user
            Console.WriteLine("Result: " & OutputNumber)

            ' Update database with operation details
            DatabaseUpdater.UpdateDatabase(OperationType, InputNumber, OutputNumber)

        Catch ex As Exception
            Console.WriteLine("Error: " & ex.Message)
        End Try
    End Sub
End Module
