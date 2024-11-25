from django.shortcuts import render, redirect
from .models import Paciente

def inicio_vista(request):
    mispacientes = Paciente.objects.all()
    return render(request, 'index.html', {'mispacientes': mispacientes})

def agendarCita(request):
    if request.method == 'POST':
        id_paciente = request.POST.get('txtid_paciente')
        nombre = request.POST.get('txtnombre')
        edad = request.POST.get('numedad')
        fecha_cita = request.POST.get('txtfecha_cita')
        hora_cita = request.POST.get('txthora_cita')
        motivo = request.POST.get('txtmotivo')

        paciente = Paciente(id_paciente=id_paciente, nombre=nombre, edad=edad, fecha_cita=fecha_cita, hora_cita=hora_cita, motivo=motivo)
        paciente.save()

        return redirect('inicio')
    return render(request, 'agendar_citas.html')

def citasAgendadas(request):
    mispacientes = Paciente.objects.all()
    return render(request, 'citas_agendadas.html', {'mispacientes': mispacientes})

def seleccionarPaciente(request, id_paciente):
    paciente = Paciente.objects.get(id_paciente=id_paciente)
    if request.method == 'POST':
        paciente.nombre = request.POST.get('nombre')
        paciente.edad = request.POST.get('edad')
        paciente.fecha_cita = request.POST.get('fecha_cita')
        paciente.hora_cita = request.POST.get('hora_cita')
        paciente.motivo = request.POST.get('motivo')

        if not paciente.nombre:
            return render(request, 'editarpaciente.html', {'paciente': paciente, 'error': 'El campo nombre es obligatorio.'})

        paciente.save()
        return redirect('inicio')

    return render(request, 'editarpaciente.html', {'paciente': paciente})


def borrarPaciente(request, id_paciente):
    paciente = Paciente.objects.get(id_paciente=id_paciente)
    paciente.delete()

    return redirect('inicio')

def actualizarPaciente(request, id_paciente):
    paciente = Paciente.objects.get(id_paciente=id_paciente)
    
    if request.method == 'POST':
        paciente.nombre = request.POST.get('nombre')
        paciente.edad = request.POST.get('edad')
        paciente.fecha_cita = request.POST.get('fecha_cita')
        paciente.hora_cita = request.POST.get('hora_cita')
        paciente.motivo = request.POST.get('motivo')
        paciente.save()

        return redirect('inicio')
    
    return render(request, 'actualizar_paciente.html', {'paciente': paciente})
