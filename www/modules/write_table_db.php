<?php 
// include 'database.php';
    #Namen der Reifetabelle in db speichern
    if (isset ($_POST['choose_agingtable'])){
        $chosen_agingtable = $_POST['agingtable'];
        write_agingtable($chosen_agingtable);
        $logstring = 'selected agingtable "' . $chosen_agingtable . '"';
        logger('INFO', $logstring );
        print '<script language="javascript"> alert("'. (_("agingtable")) . " : " . $chosen_agingtable . ' ' . (_("is selected")) .'"); </script>';
    }
    if (isset ($_POST['edit_agingtable'])){
        $edit_agingtable = $_POST['agingtable_edit'];
        // write_agingtable($chosen_agingtable);
        $logstring = 'button edit agingtable pressed';;
        logger('DEBUG', $logstring );
        print '<script language="javascript"> alert("'. (_("button")) . " : " . (_("no buttonfunction")) .'"); </script>';
    }
    if (isset ($_POST['delete_agingtable'])){
        $edit_agingtable = $_POST['agingtable_edit'];
        $returncode = delete_agingtable($edit_agingtable);
        $logstring = 'button delete agingtable pressed';
        logger('DEBUG', $logstring );
        if ($returncode == TRUE){
            print '<script language="javascript"> alert("'. (_("agingtable")) . " : " . (_("agingtable")) . ' ' . $edit_agingtable . ' ' . (_("deleted")) . '"); </script>';
        }
        elseif ($returncode == FALSE){
            print '<script language="javascript"> alert("'. (_("agingtable")) . " : " . $edit_agingtable . ' ' . (_("can not delete selected agingtable. Please choose an other first")) .'"); </script>';
        }
        else{
            print '<script language="javascript"> alert("'. (_("agingtable")) . " : " . (_("unexpected Error")) .'"); </script>';
        }
    }
    if (isset ($_POST['upload_new_agingtable'])){
        $edit_agingtable = $_POST['agingtable_edit'];
        // write_agingtable($edit_agingtable);
        $logstring = 'button upload new agingtable pressed';
        logger('DEBUG', $logstring );
        print '<script language="javascript"> alert("'. (_("button")) . " : " . (_("no buttonfunction")) .'"); </script>';
    }
    if (isset ($_POST['export_agingtable'])){
        $edit_agingtable = $_POST['agingtable_edit'];
        // write_agingtable($edit_agingtable);
        $logstring = 'button export  pressed';
        logger('DEBUG', $logstring );
        print '<script language="javascript"> alert("'. (_("button")) . " : " . (_("no buttonfunction")) .'"); </script>';
    }
?>
