$(document).ready(function () {
    // show modal (show.bs.modal : 모달이 사용자에게 보여졌을 때 아래의 옵션을 적용)
    $('#task-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // 모달 윈도우를 오픈하는 버튼
        const taskID = button.data('source') // 버튼에서 data-source 값을 taskID에 저장
        const des = button.data('contents')
        const dd = button.data('content')
        const detail = button.data('detail')
        console.log(button.data())
        const modal = $(this)
        if (taskID === 'New Task') {
            modal.find('.modal-title').text(taskID) // 모달 윈도우에서 .modal-title을 찾아서 taskID 값을 치환
            $('#task-form-display').removeAttr('taskID')
        } else {
            modal.find('.modal-title').text('Edit Task ')
            $('#task-form-display').attr('taskID', taskID)
        }

        if (des) {
            modal.find('.form-control').val(des);
            modal.find('#detail1').val(detail);
            modal.find('#date1').val(dd)
        } else {
            modal.find('.form-control').val('');
        }
    })


    $('#detail-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget)
        const task = button.data('source')
        var det = button.data('contents')
        const dd = button.data('content')
        console.log(button.data())
        const modal = $(this)
        modal.find('#detail-task').text(task)
        modal.find('#detail-detail').text(det)
        modal.find('#detail-date').text(dd)
    })



    $('#sd').click(function(){
        const sd = $(this)
        stat=sd.data('source')
        console.log(sd.data('source'))
        $.ajax({
            type: 'POST',
            url: '/home',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                "sort" : "2"
            }),
            success: function (res) {
                console.log(res.response)

            },
            error: function (){
                console.log('Error');
            }
        });
    })

    $('#sr').click(function(){
        const sr = $(this)
        console.log(sr.data('source'))
        stat = sr.data('source')
        $.ajax({
            type: 'POST',
            url: '/home',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                "sort" : "1"
            }),
            success: function (res) {
                console.log(res.response)
            },
            error: function (){
                console.log('Error');
            }
        });
    })




    $('#submit-task').click(function () {
        const target = $(this)
        const tID = $('#task-form-display').attr('taskID');
        console.log($('#task-modal').find('#detail1').val())
        $.ajax({
            type: 'POST',
            url: tID ? '/edit/' + tID : '/create',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#task-modal').find('.form-control').val(),
                'detail': $('#task-modal').find('#detail1').val(),
                'due_date': $('#task-modal').find('#date1').val(),
                'user' : target.data('source')
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();

            },
            error: function () {
                console.log('Error');
            }
        });
    });



    $('#delete-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const taskID = button.data('source')
        console.log(button.data())
            $('#delete-task').click(function () {
                $.ajax({
                    type: 'POST',
                    url: '/delete/' + taskID,
                    success: function (res) {
                        console.log(res.response)
                        location.reload();
                    },
                    error: function () {
                        console.log('Error');
                    }
                });
            });
        })




    $('.state').click(function () {
        const state = $(this);
        const tID = state.data("source");
        console.log(tID)
        var new_state = "Todo";
        if (state.text() === "In progress") {
            new_state = "Complete";
        } else if (state.text() === "Complete") {
            new_state = "Todo";
        } else if (state.text() === "Todo") {
            new_state = "In progress";
        }

        $.ajax({
            type: 'POST',
            url: '/edit/' + tID,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'status': new_state
            }),
            success: function (res) {
                console.log(res)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });


});
